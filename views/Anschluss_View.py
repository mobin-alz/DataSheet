import sqlite3


def import_view():
    with sqlite3.connect("../data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''create view if not exists Anschluss_view  as
                            select AnschlussID, Anschl, Signalname, physikalscheAdresse, Adresse, Biatt, Funktion, Modul
                            ,ModultypeName, Pos, Unterort, Ort
                             from Anschluss_tb
                            INNER JOIN main.Modul_tb Mt on Anschluss_tb.version = Mt.version
                            INNER JOIN main.Modultype_tb M on Mt.ModultypeID = M.ModultypeID
                            INNER JOIN main.Pos_tb P on P.PosID = Mt.PosID
                            INNER JOIN main.Unterort_tb Ut on P.UnterortID = Ut.UnterortID
                            INNER JOIN main.Ort_tb Ot on Ut.OrtID = Ot.OrtID
                        ''')



