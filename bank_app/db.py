from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"  # or Atlas connection string / env var
#remeber to add this to a .env file instead of being hardcoded in

client = AsyncIOMotorClient(MONGO_URI)
db = client["bank_app"]

users_collection = db["users"]
accounts_collection = db["accounts"]
transactions_collection = db["transactions"]