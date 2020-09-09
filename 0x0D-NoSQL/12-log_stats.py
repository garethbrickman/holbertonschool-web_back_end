#!/usr/bin/env python3
""" Module for using PyMongo """

from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
col = client.logs.nginx
count = col.estimated_document_count()

print(f"{count} logs")
print("Methods:")
