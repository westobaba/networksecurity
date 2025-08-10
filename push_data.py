import os
import json
import sys
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
if not MONGO_DB_URL:
    print("Error: MONGO_DB_URL not found in .env file.")
    sys.exit(1)
print("MongoDB URL loaded from .env file:", MONGO_DB_URL)

import certifi
ca = certifi.where()

import pymongo
import pandas as pd
# No need for numpy if not used
# import numpy as np 
from networksecurity.logging.logger import logger
from networksecurity.exception.exception import NetworkSecurity

class NetworkDataExtract:
    def __init__(self):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            logger.info("Successfully connected to MongoDB.")
        except Exception as e:
            logger.error(f"Error connecting to MongoDB: {e}")
            raise NetworkSecurity(e, sys) from e

    def cv_to_json(self, file_path):
        """Converts a CSV file to a list of JSON records."""
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            # Correctly convert DataFrame to a list of dictionaries (JSON records)
            records = data.to_dict(orient='records') 
            return records
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise NetworkSecurity(f"File not found: {file_path}", sys) from FileNotFoundError
        except Exception as e:
            logger.error(f"Error in cv_to_json: {e}")
            raise NetworkSecurity(e, sys) from e

    def insert_data_mongodb(self, records, database_name, collection_name):
        """Inserts a list of records into a specified MongoDB collection."""
        try:
            db = self.mongo_client[database_name]
            collection = db[collection_name]
            collection.insert_many(records)
            logger.info(f"Successfully inserted {len(records)} records into {database_name}.{collection_name}.")
            return len(records)
        except Exception as e:
            logger.error(f"Error inserting data into MongoDB: {e}")
            raise NetworkSecurity(e, sys) from e

if __name__ == "__main__":
    # Ensure this path is correct or use a raw string
    FILE_PATH = r"network_data\phisingData.csv"
    DATABASE = "westobaba"
    COLLECTION = "NetworkData"
    try:
        networkobj = NetworkDataExtract()
        records = networkobj.cv_to_json(FILE_PATH)
        print(f"Number of records extracted: {len(records)}")
        
        # Correctly call the method with separate arguments
        no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(f"Number of records inserted: {no_of_records}")
    except NetworkSecurity as e:
        print(f"An error occurred: {e}")
        sys.exit(1)