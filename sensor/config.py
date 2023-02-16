
import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os
@dataclass

class EnvironmentalVariable:
    mongo_db_url:str =os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"
    

# Provide the mongodb localhost url to connect python to mongodb.

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


