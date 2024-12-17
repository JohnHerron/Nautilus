import sqlite3
from datetime import datetime


class Client:
    def __init__(self):
        self.con = sqlite3.connect("client.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS client (
            client_name TEXT PRIMARY KEY,
            notes TEXT,
            created_at DATE)""")

    def read_all(self):
        self.cur.execute("""SELECT * FROM client""")
        return self.cur.fetchall()

    def insert(self, data):
        self.cur.execute("""INSERT OR IGNORE INTO client VALUES (?,?,?)""",
                         data + (datetime.today().strftime('%y%m%d%H%M%S'),))
        self.con.commit()

    def update(self):
        pass

    def delete(self, name):
        self.cur.execute("""DELETE FROM client WHERE client_name = ? """, (name,))
        self.con.commit()
