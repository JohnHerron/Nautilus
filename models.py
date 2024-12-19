import sqlite3
from datetime import datetime


class Client:
    def __init__(self):
        self.con = sqlite3.connect("client.db")
        self.cur = self.con.cursor()
        self.create_table()

# TODO: Remove connections when client is deleted
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS client (
            client_name TEXT PRIMARY KEY,
            notes TEXT,
            updated_at DATE
        )""")

    def read_all(self):
        self.cur.execute("""SELECT * FROM client""")
        return self.cur.fetchall()

    def read(self, name: str):
        self.cur.execute("""SELECT * FROM client WHERE client_name = ?""", (name,))
        return self.cur.fetchall()

    def insert(self, data):
        self.cur.execute("""INSERT OR IGNORE INTO client VALUES (?,?,?)""",
                         data + (datetime.today().strftime('%y%m%d%H%M%S'),))
        self.con.commit()

    def update(self, name: str, data):
        self.cur.execute("""UPDATE client SET notes = ?, updated_at = ? WHERE client_name = ? """,
                         (data,) + (datetime.today().strftime('%y%m%d%H%M%S'), name))
        self.con.commit()

    def delete(self, name: str):
        self.cur.execute("""DELETE FROM client WHERE client_name = ? """, (name,))
        self.con.commit()


class Connection:
    def __init__(self):
        self.con = sqlite3.connect("connection.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS connection (
            connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
            connection_name TEXT NOT NULL,
            client_name TEXT,
            notes TEXT,
            updated_at DATE,
            FOREIGN KEY (client_name) REFERENCES client (client_name)
        )""")

    def read_all(self):
        self.cur.execute("""SELECT * FROM connection""")
        return self.cur.fetchall()

    def read(self, connection_id: int):
        self.cur.execute("""SELECT * FROM connection WHERE connection_id = ?""", (connection_id,))
        return self.cur.fetchall()

    def insert(self, data):
        self.cur.execute("""INSERT OR IGNORE INTO connection (connection_name, client_name, notes, updated_at) VALUES (?,?,?,?)""",
                         data + (datetime.today().strftime('%y%m%d%H%M%S'),))
        self.con.commit()

    def update(self, connection_id: int, data):
        self.cur.execute("""UPDATE connection SET connection_name = ?, notes = ?, updated_at = ? WHERE connection_id = ? """,
                         data + (datetime.today().strftime('%y%m%d%H%M%S'), connection_id))
        self.con.commit()

    def delete(self, connection_id: int):
        self.cur.execute("""DELETE FROM connection WHERE connection_id = ? """, (connection_id,))
        self.con.commit()