# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from mysql.connector import Error
from .config import DB_CONFIG
from .items import HistoricalgoldsilverItem


class HistoricalgoldsilverPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    try:
        def create_connection(self):
            self.conn = mysql.connector.connect(**DB_CONFIG)
            self.curr = self.conn.cursor()
            print('#### Connected to MySQL ####')

    except Error as e:
        print("### Error while connecting to MySQL ###:", e)

    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS gold, silver")
        self.curr.execute(
            """CREATE TABLE gold(
              metal text,
              date text, 
              price text, 
              mean text, 
              variance text)""")
        self.curr.execute(
            """CREATE TABLE silver(
              metal text,
              date text, 
              price text, 
              mean text, 
              variance text)""")

    def process_item(self, item, spider):

        metal = item.get('metal')

        if(metal == 'Gold Futures Historical Data'):
            self.store_gold(item)
        else:
            self.store_silver(item)
        return item

    def store_gold(self, item):
        self.curr.execute("""INSERT INTO gold VALUES (%s, %s, %s, %s, %s)""", (
            item['metal'],
            item['date'],
            item['price'],
            item['mean'][0],
            item['variance'][0]
        ))
        self.conn.commit()

    def store_silver(self, item):
        self.curr.execute("""INSERT INTO silver VALUES (%s, %s, %s, %s, %s)""", (
            item['metal'],
            item['date'],
            item['price'],
            item['mean'][0],
            item['variance'][0]
        ))
        self.conn.commit()
