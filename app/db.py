from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import dotenv_values
from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
config = dotenv_values('.env')

client: AsyncIOMotorClient = None
db = None 

def startup_db_client():
    global client, db
    try:
        client = MongoClient(config['DB_URL'])
        db = client.get_database('test')
        logging.info(f"DB connection success: {db}")
    except Exception as e:
        logging.error(f"DB connection error: {e}")

def shutdown_db_client():
    global client
    try:
        client.close()
        print('DB connection closed')
    except Exception as e:
        logging.error(f"DB connection close error: {e}")

def get_collection(collection_name: str):
    global db
    if db is None:
        raise Exception('DB connection not initialized')
    return db[collection_name]