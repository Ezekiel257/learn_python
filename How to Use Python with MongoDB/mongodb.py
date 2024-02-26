
from pymongo.mongo_client import MongoClient

uri = "mongodb://Zeek:Z8dh90BaT7IUqgee@atlas-sql-65c1acc8e5e7b04230d5d3e0-zwlmu.a.query.mongodb.net/?ssl=true&authSource=admin"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)