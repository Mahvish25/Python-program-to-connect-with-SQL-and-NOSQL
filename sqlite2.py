import sqlite3


connection = sqlite3.connect('sqlproject.db')


cursor = connection.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print 3 sample rows from each table
for table in tables:
    table_name = table[0]
    print(f"\nSample rows from table '{table_name}':")

    cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
    rows = cursor.fetchall()

    for row in rows:
        print(row)


cursor.close()
connection.close()
