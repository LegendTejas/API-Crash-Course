from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['mdb']
    collection = db['tejas']

    # Update the first document where name = "Tejas"
    collection.update_one(
        {"name": "Tejas"},            # Filter
        {"$set": {"name": "Tejas Tp"}}  # Update
    )

    # Update all document in collection where name ="Tejas Tp"
    collection.update_many(
        {"name": "Tejas Tp"},
        {"$set": {"marks": 100}}
    )

    # print count of how many documents are modified
    u = collection.update_many(
        {"name": "Tejas Tp"},
        {"$set": {"marks": 100}}
    )
    print(u.modified_count)