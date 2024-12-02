import sqlite3


def insert_Ort_data():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT Ort FROM data_table")
        a = cursor.fetchall()

        for item in a:
            try:
                ort_name = item[0]
                cursor.execute("""INSERT INTO Ort_tb (Ort) VALUES (?)""", (ort_name,))
                conn.commit()

            except sqlite3.IntegrityError:
                print(f"Attempted to insert duplicate OrtName: {item}. Skipping...")
                continue
