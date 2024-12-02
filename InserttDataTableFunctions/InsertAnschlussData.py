import sqlite3


def insert_Anschluss_data():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()

        cursor.execute('''SELECT "Anschl.", Signal, "Phys.Adresse", Blatt, "Funktion ", Modul , version , Adresse 
                          FROM main.data_table''')
        a = cursor.fetchall()

        old_anschl = None
        old_signal = None
        old_blatt = None
        old_funktion = None

        for item in a:
            try:
                if item[0] is not None:
                    anschl = item[0]
                    old_anschl = anschl
                else:
                    anschl = old_anschl

                if item[1] is not None:
                    signal = item[1]
                    old_signal = signal
                else:
                    signal = old_signal

                if item[2] is not None:
                    pyshcaladd = item[2]
                    old_pyshcaladd = pyshcaladd
                else:
                    pyshcaladd = old_pyshcaladd

                if item[3] is not None:
                    blatt = item[3]
                    old_blatt = blatt
                else:
                    blatt = old_blatt

                if item[4] is not None:
                    funktion = item[4]
                    old_funktion = funktion
                else:
                    funktion = old_funktion

                if item[7] is not None:
                    addr = item[7]
                    old_addr = addr
                else:
                    addr = old_addr

                modul = item[5]
                cursor.execute("SELECT ModuleId From Modul_tb WHERE Modul =?", (modul,))
                m = cursor.fetchone()
                if m is not None:
                    modul_id = m[0]
                    old_modul_id = modul_id
                else:
                    modul_id = old_modul_id

                cursor.execute("SELECT COUNT(*) FROM Anschluss_tb WHERE version =?", (item[6],))
                count = cursor.fetchone()[0]

                if count == 0:
                    query = '''INSERT INTO Anschluss_tb (Anschl,Signalname,physikalscheAdresse,Biatt,Funktion,ModulID,Adresse,version)
                        VALUES (?,?,?,?,?,?,?,?)'''
                    cursor.execute(query, (anschl, signal, pyshcaladd, blatt, funktion, modul_id, addr, item[6]))
                else:
                    print(f"Skipping insertion for version {item[6]} due to uniqueness constraint.")

            except Exception as e:
                print(f"SOME ERROR IN insert_Anschluss_data: {e}")
                continue

