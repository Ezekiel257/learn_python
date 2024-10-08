#Select the database to use.
# Select the database to use.
# Import the function to get the database.
from pymongo_get_database import get_database

# Provide the mongodb atlas url to connect python to mongodb using pymongo
from pymongo import MongoClient

# Define the function to get the database.
def get_database():
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient("mongodb+srv://Zeek:Z8dh90BaT7IUqgee@altschool.5pd9p7f.mongodb.net/")

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()


# Get the database using the method we defined in pymongo_test_insert file
dbname = get_database()
collection_name = dbname["user_1_items"]

# Inserting data into the database
item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}
collection_name.insert_many([item_1,item_2])


from dateutil import parser
expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour",
  "expiry_date" : expiry
}
collection_name.insert_one(item_3)

