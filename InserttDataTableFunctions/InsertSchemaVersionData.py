import sqlite3


def InsertSchemaVersionData(version_name, project_name):
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()

        cursor.execute('''SELECT Ort,E3ReferenceData From data_table''')
        a = cursor.fetchall()
        b = cursor.execute('''SElECT projecktID From Projeckt_tb WHERE projeckt_name = ?''', (project_name,))
        pr_res = cursor.fetchall()
        pr_id = pr_res[-1][0]
        for item in a:
            try:
                ort, programm = item
                cursor.execute('''SELECT OrtID FROM Ort_tb Where Ort = ?''', (ort,))
                ort_id_res = cursor.fetchone()

                if ort_id_res is not None:
                    ort_id = ort_id_res[0]
                    old_ort_id = ort_id

                else:
                    ort_id = old_ort_id

                if programm is not None:
                    old_programm = programm
                else:
                    programm = old_programm

                query = '''INSERT INTO SchemaVersion_tb (VersionName, Programm, OrtID, ProjecktID) VALUES (?,?,?,?)'''
                cursor.execute(query, (version_name, programm, ort_id, pr_id))

            except Exception as e:
                print(f"SOME ERROR IN insert_Schema_Version_tb: {e}")

