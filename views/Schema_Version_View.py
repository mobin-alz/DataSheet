

import sqlite3


def import_view():
    with sqlite3.connect("../data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
                create view if not exists Schema_Version_view as
                select SchemaVersion_tb.SchemaVersionID, SchemaVersion_tb.VersionName, SchemaVersion_tb.Programm, SchemaVersion_tb.save_date,P.projeckt_name, Ot.Ort, Ut.Unterort, Pt.Pos, M.Modul ,At.Anschl, At.Signalname, At.physikalscheAdresse, At.Biatt, At.Funktion, At.Adresse , At.version from SchemaVersion_tb
                INNER JOIN main.Projeckt_tb P on SchemaVersion_tb.ProjecktID = P.projecktID
                INNER JOIN main.Ort_tb Ot on Ot.OrtID = SchemaVersion_tb.OrtID
                INNER JOIN main.Unterort_tb Ut on Ot.OrtID = Ut.OrtID
                INNER JOIN main.Pos_tb Pt on Ut.UnterortID = Pt.UnterortID
                INNER JOIN main.Modul_tb M on M.PosID = Pt.PosID
                INNER JOIN main.Anschluss_tb At on M.version = At.version;
        ''')

