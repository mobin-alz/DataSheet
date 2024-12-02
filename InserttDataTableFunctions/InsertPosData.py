import sqlite3


def insert_POS_data():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()

        cursor.execute('''SELECT DISTINCT "POS.", Unterort , version FROM data_table''')
        a = cursor.fetchall()

        for item in a:
            try:
                pos_name, unterort, version = item
                cursor.execute("SELECT UnterortID FROM Unterort_tb WHERE Unterort = ? ", (unterort,))
                unterortid = cursor.fetchone()
                cursor.execute("INSERT INTO Pos_tb (Pos,UnterortID,version) VALUES (?,?,?)",
                               (pos_name, unterortid[0], version))

            except Exception as e:
                print(f"SOME ERROR IN insert_POS_data {e}")

            except sqlite3.IntegrityError:
                print(f"Attempted to insert duplicate POS: {item}. Skipping...")
