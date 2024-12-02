import sqlite3


def import_view():
    with sqlite3.connect("../data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''create view if not exists  ModulTyp_view as 
                        select ModultypeName from Modultype_tb;''')
