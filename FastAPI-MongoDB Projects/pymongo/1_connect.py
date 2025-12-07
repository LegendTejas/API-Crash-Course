from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['mdb']
    collection = db['tejas']