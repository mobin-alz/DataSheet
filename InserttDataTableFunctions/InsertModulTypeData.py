import sqlite3


def insert_moduletype_data():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT DISTINCT Typ FROM main.data_table''')
        a = cursor.fetchall()

        for typ in a[1:]:
            try:
                cursor.execute("""INSERT INTO Modultype_tb (ModultypeName) VALUES (?)""", (typ[0],))
                conn.commit()
            except sqlite3.IntegrityError:
                print(f"Attempted to insert duplicate ModultypeName: {typ}. Skipping...")
                continue
