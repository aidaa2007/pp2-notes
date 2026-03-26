import psycopg2
from config import load_config

def connect():
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50),
                phone VARCHAR(20) NOT NULL
            )
        """)
        conn.commit()
        cur.close()
        return conn
    except Exception as e:
        print(e)
        return None
