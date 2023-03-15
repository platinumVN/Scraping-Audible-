############################
# Load environment variables
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = f'{Path(__file__).resolve().parents[4]}' + '\private_env.env'
# dotenv_path = f
print(dotenv_path)
# dotenv_path = r'C:\Users\ANH THU\OneDrive\CODE\scrapers\env.env'

load_dotenv(dotenv_path=dotenv_path)
# "C:\Users\ANH THU\OneDrive\CODE\scrapers\env_vars.env"

CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')
print(CONNECTION_STRING)

import pymongo
# client = pymongo.MongoClient("mongodb+srv://thuphan:Ll3uxKE8yr6Vecb6@clusterthuscraping.pytlyml.mongodb.net/?retryWrites=true&w=majority")
# db = client['Audible']

# print(db)
# print(db.get_collection())