from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import dotenv_values
from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
config = dotenv_values('.env')

client: AsyncIOMotorClient = None
collection = None 

def startup_db_client():
    global client, collection
    try:
        client = MongoClient(config['DB_URL'])
        collection = client.get_database('test')
        logging.info(f"DB connection success: {collection}")
    except Exception as e:
        logging.error(f"DB connection error: {e}")

def shutdown_db_client():
    global client
    try:
        client.close()
        print('DB connection closed')
    except Exception as e:
        logging.error(f"DB connection close error: {e}")
