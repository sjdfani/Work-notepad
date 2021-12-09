import sqlite3


def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS university (frame text,class text,detail text,icon text,link text)")
    conn.commit()
    conn.close()


def insert(frame, className, detail, icon, link):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO university VALUES (?,?,?,?,?)",
                (frame, className, detail, icon, link))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM university")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_frame(frame=""):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM university WHERE frame=? ",
                (frame,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(frame):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM university WHERE frame=?", (frame,))
    conn.commit()
    conn.close()


def update(frame, className, detail, icon, link):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE university SET class=?,detail=?,icon=?,link=? WHERE frame=?",
                (className, detail, icon, link, frame))
    conn.commit()
    conn.close()


connect()
