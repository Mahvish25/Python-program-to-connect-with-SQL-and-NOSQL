from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['PythonProject']

collections = db.list_collection_names()

sample_size = 3

for collection_name in collections:
    collection = db[collection_name]
    print(f"\nSample documents from collection '{collection_name}':")

    sample_documents = collection.find().limit(sample_size)

    for doc in sample_documents:
        print(doc)


client.close()
