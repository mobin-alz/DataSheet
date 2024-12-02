import sqlite3


def insert_Unterort_data():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT Ort, Unterort FROM data_table")
        a = cursor.fetchall()

        for item in a:
            try:
                cursor.execute("SELECT OrtID From Ort_tb Where Ort =?", (item[0],))
                ort_id_tuple = cursor.fetchone()
                if ort_id_tuple[0] is not None:
                    ort_id = ort_id_tuple[0]
                    old_ort_id = ort_id
                else:
                    ort_id = old_ort_id
                cursor.execute("INSERT INTO Unterort_tb (Unterort, OrtID) VALUES (?,?)", (item[1], ort_id))

            except Exception as e:
                print(f"SOME ERROR IN insert_Unterort_data {e}")
                continue

            except sqlite3.IntegrityError:
                print(f"Attempted to insert duplicate Unterort: {item}. Skipping...")
