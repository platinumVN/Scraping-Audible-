# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

############################
# Load environment variables
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(f'{Path(__file__).resolve().parents[1]}\env_vars.env')
load_dotenv(dotenv_path=dotenv_path)

CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')

###############
#Define classes

import logging
class ScrapingAudiblePipeline:
    """The default examle
    """
    def open_spider(self, spider):
        logging.warning('Spider Opened - Pipeline')
    def close_spider(self, spider):
        logging.warning('Spider Closed - Pipeline')
    def process_item(self, item, spider):
        return item

import pymongo

class MongodbPipeline:
    """MongoDB
    """
    collection_name = 'AudibleScrapy'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(CONNECTION_STRING)
        self.db = self.client['Audible']
    def close_spider(self, spider):
        self.client.close()
        logging.warning('MongoClient Closed - Pipeline')
    def process_item(self, item, spider):
        logging.warning('Add item - MongoDB Pipeline')
        self.db[self.collection_name].insert_one(item)
        return item
