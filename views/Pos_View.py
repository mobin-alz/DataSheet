import sqlite3


def import_view():
    with sqlite3.connect("../data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''create view if not exists  Pos_view as 
                          select DISTINCT Pos , Unterort , Ort from Pos_tb
                          INNER JOIN main.Unterort_tb Ut on Pos_tb.UnterortID = Ut.UnterortID
                          INNER JOIN main.Ort_tb Ot on Ut.OrtID = Ot.OrtID
                           ''')

