#!/usr/bin/env python3
"""module that lists all documents in a collection"""


def list_all(mongo_collection):
    """ lists all documents in a collection 
    arg: mongo_collectio -> pymongo collection object"""
    result = list(mongo_collection.find())

    if len(result) == 0:
        return []
    return result
