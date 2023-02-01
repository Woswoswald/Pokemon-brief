import json
from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient("mongodb://admin:password@localhost:27017/")

# Select the database and collection
db = client["pokemon"]
collection = db["JDG"]

with open("pokemon.json") as file:
    data = json.load(file)

if isinstance(data, list):
    collection.insert_many(data) 
else:
    collection.insert_one(data)

# Function to create a new document
def create_document(document):
    collection.insert_one(document)
    print("Document created successfully.")

# # Call the function to create a new document
new_document = { "id": 899, "pokedexId": 899, "name": "Darty Papa", "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923", "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows", "slug": "Darty Papa", "stats": { "HP": 100000000, "attack": 100000000, "defense": 2, "special\_attack": 100000000, "special\_defense": 2, "speed": 1 }

}
create_document(new_document)

#Function to update a document
def update_document(filter, update):
    collection.update_one(filter, {"$set": update})
    print("Document updated successfully.")

filter = {"name": "Darty Papa"}
update = {"slug": "newslug"}
update_document(filter, update)

# Function to delete a document
def delete_document(filter):
    collection.delete_one(filter)
    print("Document deleted successfully.")

filter = {"name": "Darty Papa"}
delete_document(filter)

documents = list(collection.find({}))

# Write the contents to a JSON file
with open("pokemon_collection.json", "w") as file:
    json.dump(documents, file, default=str, indent=4)

print("Database exported successfully.")