import sqlite3

connection = sqlite3.connect('sqlproject.db')

cursor = connection.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the number of rows in each table
for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    print(f"Table '{table_name}' has {row_count} rows.")

connection.commit()
connection.close()
