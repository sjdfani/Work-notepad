import sqlite3


def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY ,title text ,description text,date text,state text)")
    conn.commit()
    conn.close()


def insert(title, description, date, state):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO history VALUES (NULL ,?,?,?,?)",
                (title, description, date, state))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM history")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_id(ID=""):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM history WHERE id=? ",
                (ID,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(ID):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM history WHERE id=?", (ID,))
    conn.commit()
    conn.close()


connect()
