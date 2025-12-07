from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")

    db = client['mdb']
    collection = db['tejas']
    
    # find one
    find_one = collection.find_one({'name': 'Jill'})
    print(find_one)

    print("\n")

    # find Tejas in all documents
    allDocs = collection.find({'name': 'Tejas Tp'})
    for item in allDocs:
        print(item)

    print("\n")

    # show documents where marks <= 90
    for doc in collection.find({'marks': {'$lte': 90}}):
        print(doc)

    print("\n")

    # show documents where marks > 95
    for doc in collection.find({'marks': {'$gt': 95}}):
        print(doc)

    print("\n")

    # show all rows (documents) in the collection
    for doc in collection.find():
        print(doc)

    # count total documents (rows) in the collection
    print("\nTotal Rows:", collection.count_documents({}))