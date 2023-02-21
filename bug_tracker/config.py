import pymongo
import os
# Provide the mongodb localhost url to connect python to mongodb.
mongo_client = pymongo.MongoClient("mongodb+srv://prasadilla42:bugcreate12345@bugtracker.quievi7.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME = "BUGCREATETRACKER"
bug_tracker_db = mongo_client[DATABASE_NAME]
