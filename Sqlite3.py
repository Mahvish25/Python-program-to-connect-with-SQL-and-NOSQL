import sqlite3

connection = sqlite3.connect('sqlproject.db')

cursor = connection.cursor()

#Performing a full outer join using SQLite.

query = """
SELECT Comments.Comment_ID, Comments.N_of_comment AS COMM, Videos.Video_Id, Videos.Length AS Len
From Comments
LEFT JOIN Videos ON Comments.Comment_ID = Videos.Length

UNION

SELECT Comments.Comment_ID, Comments.N_of_comment AS COMM, Videos.Video_Id, Videos.Length AS Len
From Videos
LEFT JOIN Comments ON Videos.Length = Comments.Comment_ID
WHERE Comments.Comment_ID IS NULL
"""

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()

connection.close()
