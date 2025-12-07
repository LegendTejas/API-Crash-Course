# PyMongo

PyMongo is the official Python driver for MongoDB, a popular NoSQL document database. 

It lets Python programs connect to MongoDB and perform database operations like inserting, querying, updating, and deleting data.

---

## What MongoDB Is

MongoDB stores data in documents (JSON-like objects) instead of tables and rows.
Example document:

```
{
  "_id": 1,
  "name": "Alice",
  "age": 25
}
```

These documents are stored inside collections, which are like tables.

---

## What PyMongo Does

PyMongo acts as the bridge between Python and MongoDB. It allows you to:

- Connect to a MongoDB server

- Create databases & collections

- Insert documents

- Query data

- Update data

- Delete data

---

### Installing PyMongo
```
pip install pymongo
```

### Basic Connection Example

```
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["students"]
```

`client` → connects to MongoDB

`db` → selects a database

`collection` → selects a collection

### Insert Data
```
student = {"name": "John", "age": 21}
collection.insert_one(student)
```

### Find Data
```
for doc in collection.find():
    print(doc)
```

Find one document:

```
collection.find_one({"name": "John"})
```

### Update Data
```
collection.update_one(
    {"name": "John"},
    {"$set": {"age": 22}}
)
```

### Delete Data
```
collection.delete_one({"name": "John"})
```

---

## mongo v/s mongod

- mongod is the "Mongo Daemon" it's basically the host process for the database ("start the MongoDB process and run it in the background")

- mongod has several default parameters, such as storing data in /data/db and running on port 27017.

- mongo is the command-line shell that connects to a specific instance of mongod.

- when you run mongo with no parameters it defaults to connecting to the localhost on port 27017.