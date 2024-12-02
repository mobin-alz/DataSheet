import sqlite3


def import_view():
    with ((sqlite3.connect("../data.db"))):
        cursor = conn.cursor()
        cursor.execute(
                            '''create view if not exists  Modul_View  as
                            select ModuleId , ModultypeName , Modul , Pos , Unterort , Ort from Modul_tb
                            INNER JOIN main.Modultype_tb Mt on Modul_tb.ModultypeID = Mt.ModultypeID
                            INNER JOIN main.Pos_tb Pt on Modul_tb.PosID = Pt.PosID
                            INNER JOIN main.Unterort_tb Ut on Pt.UnterortID = Ut.UnterortID
                            INNER JOIN main.Ort_tb Ot on Ut.OrtID = Ot.OrtID
                            '''
        )
