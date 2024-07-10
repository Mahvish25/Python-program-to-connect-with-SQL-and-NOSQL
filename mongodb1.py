from pymongo import MongoClient

# Replace the connection string with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/')

# Access the database
db = client['PythonProject']

# Iterate over all collections in the database
collection_names = db.list_collection_names()

# Access the collection
collection = db['Channel']

#Count of rows of each collection
for collection_name in collection_names:
    collection = db[collection_name]
    count = collection.count_documents({})
    print(f"Collection '{collection_name}' has {count} documents.")
