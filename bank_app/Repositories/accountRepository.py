from decimal import Decimal

from ..db import accounts_collection
from bson import ObjectId



#Class responsible for storage of accounts
class AccountRepository:

    async def create(self, accountDc: dict) -> str:
        result = await accounts_collection.insert_one(accountDc)
        return str(result.inserted_id)
    
    async def getById(self, accountId: str) -> dict | None:
        return await accounts_collection.find_one({"_id": ObjectId(accountId)})
    
    async def getAllForUser(self, userId:str) -> list[dict]:
        cursor = accounts_collection.find({"userId": userId})
        return [dc async for dc in cursor]
    
    async def updateBalance(self, accountId:str, delta: Decimal) -> None:
        await accounts_collection.update_one(
            {"_id": ObjectId(accountId)},
             {"$inc": {"balance": float(delta)}}
        )
    
    async def addTransaction(self, accountId: str, transactionDc: dict) -> None:
        await accounts_collection.update_one(
            {"_id": ObjectId(accountId)},
            {"$push": {"transactions": transactionDc}}
        )
    #method to save created account to local list
    #def save(account):
       # accounts.append(account)
        #return account
    
    #method to retrieve all accounts
    #def findAll():
        #return accounts