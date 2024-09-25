from contextlib import contextmanager
from config import get_db_connection

@contextmanager
def db_connection():
    conn = None
    try:
        conn = get_db_connection()
        yield conn
    except Exception as e:
        if conn:
            conn.rollback()  # Roll back any open transaction in case of an error
        raise e  # Re-raise the exception after handling
    finally:
        if conn:
            conn.close()  # Always close the connection
