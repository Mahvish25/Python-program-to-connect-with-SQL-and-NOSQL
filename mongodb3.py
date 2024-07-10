from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['PythonProject']

# Performs a left outer join to the Videos collection
# Define the aggregation pipeline
pipeline = [
    {
        "$lookup": {
            "from": "Videos",
            "localField": "Comment_ID",
            "foreignField": "Comm_ID",
            "as": "Videos"
        }
    }
]

result = db.Comments.aggregate(pipeline)

for doc in result:
    print(doc)

client.close()
