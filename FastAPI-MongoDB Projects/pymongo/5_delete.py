from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['mdb']
    collection = db['tejas']

    # delete one
    collection.delete_one({"_id": 6})

    # delete many
    # Delete all documents where name = "Tejas Tp"
    result = collection.delete_many({"name": "Tejas Tp"})

    print("Deleted Documents:", result.deleted_count)  # Show how many were deleted