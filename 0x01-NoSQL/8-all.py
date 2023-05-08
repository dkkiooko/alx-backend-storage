#!/usr/bin/env python3
"""module that lists all documents in a collection"""
from pymongo import MongoClient


client = MongoClient()

def list_all(mongo_collection):
    """ lists all documents in a collection 
    arg: mongo_collectio -> pymongo collection object"""
    result = mongo_collection.find()

    if result.count() == 0:
        return []
    return result
