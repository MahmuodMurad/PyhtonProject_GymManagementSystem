import  sqlite3

conn = sqlite3.connect("app_db.db")
c = conn.cursor()





c.execute("DELETE FROM players_datas WHERE name = 'OmarEbrahimOmar'")
print("delete")
conn.commit()
conn.close()