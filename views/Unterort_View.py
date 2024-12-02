import sqlite3


def import_view():
    with sqlite3.connect("../data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''create view if not exists  Unterort_view as 
                          select DISTINCT Ort , Unterort from Unterort_tb
                          INNER JOIN main.Ort_tb Ot on Unterort_tb.OrtID = Ot.OrtID
                          ''')