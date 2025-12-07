from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")

    # show databases
    allDatabases = client.list_database_names()
    print(allDatabases)
    # print(", ".join(allDatabases))   # prints as a single string

    # show collections
    db = client["mdb"]
    allCollections = db.list_collection_names()
    print("\n",allCollections)