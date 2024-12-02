def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Modultype_tb (  
                        ModultypeID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ModultypeName varchar(60) UNIQUE NOT NULL
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Ort_tb (
                        OrtID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Ort varchar(60) UNIQUE NOT NULL)
                        ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Unterort_tb (
            UnterortID INTEGER PRIMARY KEY AUTOINCREMENT,
            Unterort varchar(60) NOT NULL,
            OrtID INTEGER NOT NULL,
            FOREIGN KEY(OrtID) REFERENCES Ort_tb(OrtID)
            )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Pos_tb (
                        PosID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Pos varchar(60) NOT NULL,
                        UnterortID INTEGER,
                        version INTEGER UNIQUE,
                        FOREIGN KEY(UnterortID) REFERENCES Unter_tb(UnterortID)
                        )''')

    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Modul_tb (
                        ModuleId INTEGER PRIMARY KEY AUTOINCREMENT,
                        Modul varchar(60),
                        ModultypeID INTEGER,
                        PosID INTEGER ,
                        version INTEGER UNIQUE,
                        FOREIGN KEY(ModultypeID) REFERENCES Modultype_tb(ModultypeID),
                        FOREIGN KEY(PosID) REFERENCES Pos_tb(PosID)
                        )
                    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Anschluss_tb (
                        AnschlussID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Anschl varchar(50),
                        Signalname varchar(50),
                        physikalscheAdresse varchar(80),
                        Biatt INTEGER,
                        Funktion Char(10),
                        Adresse TEXT,
                        ModulID INTEGER,
                        version INTEGER UNIQUE,
                       FOREIGN KEY(ModulID) REFERENCES Modul_tb(ModuleID))''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Projeckt_tb(
                        projecktID INTEGER PRIMARY KEY AUTOINCREMENT,
                        projeckt_name varchar(60) Not Null
                    )
    
    ''')

    cursor.execute('''
                              CREATE TABLE IF NOT EXISTS SchemaVersion_tb(
                              SchemaVersionID INTEGER PRIMARY KEY AUTOINCREMENT,
                              VersionName varchar(60) NOT NULL,
                              Programm varchar(60),
                              save_date Date DEFAULT CURRENT_DATE,
                              OrtID INTEGER NOT NULL,
                              ProjecktID INTEGER NOT NULL,
                              FOREIGN KEY (OrtID) REFERENCES Ort_tb(OrtID),
                              FOREIGN KEY (ProjecktID) REFERENCES Projeckt_tb(projecktID)
                              )
                   ''')
