from tkinter import messagebox

from InserttDataTableFunctions.InsertAnschlussData import insert_Anschluss_data
from InserttDataTableFunctions.InsertModulFunction import insert_Module_data
from InserttDataTableFunctions.InsertModulTypeData import insert_moduletype_data
from InserttDataTableFunctions.InsertOrtData import insert_Ort_data
from InserttDataTableFunctions.InsertPosData import insert_POS_data
from InserttDataTableFunctions.InsertUnterOrtData import insert_Unterort_data


def exportdatabase():
    try:
        print('text')
        # Insertion
        insert_moduletype_data()
        print(1)
        insert_Ort_data()
        print(2)
        insert_Unterort_data()
        print(3)
        insert_POS_data()
        print(4)
        insert_Module_data()
        print(5)
        insert_Anschluss_data()
        print(6)
        messagebox.showinfo(title="Success", message="Data exported to Database successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred ExportDatabase File : {e}")
