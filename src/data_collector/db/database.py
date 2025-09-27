from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from data_collector.configs import mongo


client = AsyncIOMotorClient(mongo.MONGO_URI, server_api=ServerApi("1"))
db = client[mongo.COLLECTION]
