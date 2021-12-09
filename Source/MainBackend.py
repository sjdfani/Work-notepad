import sqlite3


def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS main (id INTEGER PRIMARY KEY ,frame text,title text ,description text,date text,state text,file text)")
    conn.commit()
    conn.close()


def insert(frame, title, description, date, state, file):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO main VALUES (NULL ,?,?,?,?,?,?)",
                (frame, title, description, date, state, file))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM main")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_frame(frame1=""):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM main WHERE frame=? ",
                (frame1,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(frame):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM main WHERE frame=?", (frame,))
    conn.commit()
    conn.close()


def update(ID, frame, title, description, date, state, file):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE main SET frame=?,title=?,description=?,date=?,state=?,file=? WHERE id=?",
                (frame, title, description, date, state, file, ID))
    conn.commit()
    conn.close()


connect()
