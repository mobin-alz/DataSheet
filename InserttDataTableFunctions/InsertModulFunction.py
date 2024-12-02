import sqlite3


def insert_Module_data():
    with (sqlite3.connect("data.db") as conn):
        cursor = conn.cursor()

        cursor.execute('''SELECT Modul,"Pos.",Typ, version from data_table ''')
        a = cursor.fetchall()
        for item in a:
            try:
                cursor.execute('''SELECT ModultypeID From Modultype_tb WHERE ModultypeName = ? ''', (item[2],))
                x = cursor.fetchone()
                if x is not None:
                    modultypeid = x[0]
                    old_modultypeid = modultypeid
                else:
                    modultypeid = old_modultypeid

                cursor.execute('''SELECT PosID From Pos_tb WHERE Pos = ?''', (item[1],))
                y = cursor.fetchone()
                if y is not None:
                    pos = y[0]
                    old_pos = pos

                else:
                    pos = old_pos

                if item[0] is not None:
                    modul = item[0]
                    oldmodul = modul
                else:
                    modul = oldmodul

                query = "INSERT INTO Modul_tb ( Modul,PosID,ModultypeID,version) VALUES (?,?,?,?)"
                cursor.execute(query, (modul, pos, modultypeid, item[3]))

            except sqlite3.IntegrityError:
                print(f"Attempted to insert duplicate Modul : {item}. Skipping...")
                continue

            except Exception as e:
                print(f"SOME ERROR IN insert_Module_data {e}")
