import sqlite3


def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS TableTab (frame text,title text,detail text,icon text,states text)")
    conn.commit()
    conn.close()


def insert(frame, title, detail, icon, states):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO TableTab VALUES (?,?,?,?,?)",
                (frame, title, detail, icon, states))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TableTab")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_frame(frame=""):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TableTab WHERE frame=? ",
                (frame,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(frame):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM TableTab WHERE frame=?", (frame,))
    conn.commit()
    conn.close()


def update(frame, title, detail, icon, states):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE TableTab SET title=?,detail=?,icon=?,states=? WHERE frame=?",
                (title, detail, icon, states, frame))
    conn.commit()
    conn.close()


connect()
