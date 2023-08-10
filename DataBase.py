import sqlite3

class DataBase:
    #constructor for connection
    def __init__(self,db): 
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS players_datas( id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,phone TEXT,i_d TEXT,address TEXT,paidUp TEXT,paymentDate TEXT,renewDate TEXT,email TEXT,tyPe TEXT,subtype TEXT)""")
        self.conn.commit()
        
    # اللى هتاخد بيانات اللاعب وتضيفها فى الداتابيز    
    def insert(self,name,phone,i_d,address,paidUp,paymentDate,renewDate,email,tyPe,subtype):
        
        self.c.execute("INSERT INTO players_datas (name,phone,i_d,address,paidUp,paymentDate,renewDate,email,tyPe,subtype) VALUES (?,?,?,?,?,?,?,?,?,?)",(name,phone,i_d,address,paidUp,paymentDate,renewDate,email,tyPe,subtype))
        
        self.conn.commit()
    # الخاصة ب زرار أبديت بيانات اللاعب    
    def update(self,name,phone,i_d,address,paidUp,paymentDate,renewDate,email):
        self.c.execute("UPDATE players_datas SET name = ?, phone = ?, i_d = ?, address = ?, paidUp = ?, paymentDate = ?, renewDate = ?,email = ? , WHERE name = ? ",
                  (name,phone,i_d,address,paidUp,paymentDate,renewDate,email))
        self.conn.commit()
    # اللى هتبحث عن لاعب ب اسمه وتعرضه جوا ال gui     
    def fetch_view(self,name):
        self.c.execute("SELECT * FROM players_datas WHERE name = ?", (name,))
        row = self.c.fetchone()
        return row
     # حذف اللاعب ب اسمه   
    def delete(self,name):
        self.c.execute("DELETE FROM players_datas WHERE name=?", (name,))
        self.conn.commit()
        
    # عرض جميع اللاعبين 
    def fetch_all(self):
        self.c.execute("SELECT * FROM players_datas ")
        rows = self.c.fetchall()
        return rows
        
    def __del__(self):
        self.conn.close()
        
# ده متغير بيعبر عن ملف الداتابيز بتاع الكونكشن       


db = DataBase("app_db.db")


##########################################################
#كل صفحة ليها فانكشن من دول هتيجى فى أول الصفحة وتكتب كده

#from db import DataBase
#db = DataBase("app_db.db")





        