from pymongo import MongoClient

client = MongoClient("mongodb://admin:adminpass@mongo:27017/")
db = client["demo"]
collection = db["users"]

name = input("Enter your name: ")

collection.insert_one({"name": name})

print(f"Saved {name} to MongoDB")


