from pymongo import MongoClient
from urllib.parse import quote_plus

username = "sahiljal751_db_user"
password = quote_plus("sahiljal%8094")

uri = f"mongodb+srv://{username}:{password}@cluster0.9eobqtg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)