import os
import pymongo
import time
import random

client = pymongo.MongoClient(os.environ['CHANGE_STREAM_DB'])
while True:
    print(client.changestream.collection.insert_one({"temperature": random.random() * 100}).inserted_id)
    time.sleep(0.050)
