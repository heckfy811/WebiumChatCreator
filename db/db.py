import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mentors (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)
    conn.commit()
    conn.close()

def save_mentor(user_id: int, name: str):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO mentors (user_id, name) VALUES (?, ?)", (user_id, name))
    conn.commit()
    conn.close()

def get_mentor(user_id: int) -> str | None:
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM mentors WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None