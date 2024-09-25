from db_connection import get_db_connection

# Path to your tables.sql file
sql_file_path = 'tables.sql'

# Function to execute SQL from file
def execute_sql_file(file_path):
    conn = None
    try:
        # Get the database connection from db_connection.py
        conn = get_db_connection()
        cur = conn.cursor()

        # Read SQL file
        with open(file_path, 'r') as f:
            sql_content = f.read()

        # Execute the SQL content
        cur.execute(sql_content)
        conn.commit()
        print(f"SQL script {file_path} executed successfully.")
    
    except Exception as e:
        print(f"Error executing SQL file: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
    
    finally:
        if conn:
            cur.close()
            conn.close()

# Run the script to execute the SQL file
execute_sql_file(sql_file_path)
