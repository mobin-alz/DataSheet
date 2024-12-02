import sqlite3

import tkinter as tk
import tkinter.font as fnt
from tkinter import filedialog, messagebox, simpledialog

import pandas as pd

from DataBaseTables.Create_Tables import create_tables
from ImportExportDB.ExportDatabase import exportdatabase
from InserttDataTableFunctions.InsertSchemaVersionData import InsertSchemaVersionData

projeckt_names = []


def load_and_merge_files():
    try:
        file_paths = filedialog.askopenfilenames(title="Select Excel files", filetypes=[("Excel files", "*.xlsx")])
        if len(file_paths) < 2:
            messagebox.showerror("Error", "Please select at least two Excel files.")
            return

        projeckt_name = simpledialog.askstring("Input", "Enter the projeckt name:")

        if not projeckt_name:
            messagebox.showerror("Error", "Projeckt name cannot be empty.")
            return

        else:
            projeckt_names.append(projeckt_name)

        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            create_tables(conn)

            cursor.execute('''INSERT INTO Projeckt_tb (projeckt_name) VALUES (?)''', (projeckt_name,))
            conn.commit()
            dataframes = [pd.read_excel(fp) for fp in file_paths]
            combined_df = pd.concat(dataframes).reset_index(drop=True)
            combined_df.insert(0, 'version', range(100, 100 + len(combined_df)))
            unique_combined_df = combined_df.drop_duplicates(subset=['version'], keep='first')
            unique_combined_df.to_sql(name='data_table', con=conn, if_exists='replace', index=False)
            messagebox.showinfo(title='Success', message="Data loaded and stored in SQLite database named 'data.db'")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred load_data .: {e}")


def export_data():
    try:
        schema_version_name = simpledialog.askstring("Input", "Enter the schema version name:")
        if not schema_version_name:
            messagebox.showerror("Error", "Project name cannot be empty.")
            return

        with sqlite3.connect("data.db") as conn:
            df = pd.read_sql_query(sql="SELECT * FROM data_table", con=conn)
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

            if file_path:
                df.to_excel(file_path, index=False)
                df.to_sql(name='data_table', con=conn, if_exists='replace', index=False)
                messagebox.showinfo(title="Success", message="Data exported to Excel successfully.")

        InsertSchemaVersionData(schema_version_name, projeckt_names[0])

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred export_data: {e}")


window = tk.Tk()
window.title("FormatCombi")
window.geometry("800x650")
window.config(bg="#f0f0f0")
font_style = fnt.Font(family="Arial", size=12)

load_button = tk.Button(window, text="Load and Merge Excel Files",
                        bg="#f0f0f0", fg="black", relief=tk.RAISED, command=load_and_merge_files)
load_button.pack(pady=30, padx=30, ipadx=25, ipady=15)

export_button = tk.Button(window, text="Export Data as Excel File",
                          bg="#008B00", activebackground="#008B00", font=font_style, fg="white", bd=2,
                          command=export_data)

export_data = tk.Button(window, text="Click to Export Data on Database",
                        bg="#008B00", activebackground="#008B00", font=font_style, fg="white",
                        command=exportdatabase)

export_data.pack(pady=30, padx=60, ipadx=0, ipady=10)
export_button.pack(pady=30, padx=30, ipadx=25, ipady=10)

window.mainloop()
