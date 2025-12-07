from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['mdb']
    collection = db['tejas']

    #insert one
    collection.insert_one(
        {
            'name': 'Tejas',
            'subject': 'Maths',
            'marks': 100
        }
    )
    
    #insert many
    collection.insert_many([
        {'_id':2, 'name': 'John','subject': 'English','marks': 85},
        {'_id':3, 'name': 'Rohan','subject': 'Physics','marks': 67},
        {'_id':4, 'name': 'Jill','subject': 'Biology','marks': 99},
        {'_id':5, 'name': 'Sachin','subject': 'Hindi','marks': 89},
        {'_id':6, 'name': 'Tejas Tp','subject': 'Chemistry','marks': 90}


    ])