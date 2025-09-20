import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="localhost",
        port=5432
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS mentors (
        id SERIAL PRIMARY KEY,
        tg_id BIGINT UNIQUE NOT NULL,
        mentor_name TEXT,
        refresh_token TEXT
    );
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_mentor(tg_id: int, mentor_name: str, refresh_token: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO mentors (tg_id, mentor_name, refresh_token)
        VALUES (%s, %s, %s)
        ON CONFLICT (tg_id) DO UPDATE
        SET mentor_name = EXCLUDED.mentor_name,
            refresh_token = EXCLUDED.refresh_token;
    """, (tg_id, mentor_name, refresh_token))
    conn.commit()
    cur.close()
    conn.close()


def get_mentor(tg_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mentors WHERE tg_id = %s", (tg_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row