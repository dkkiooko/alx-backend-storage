#!/usr/bin/env python3
"""insert new document in collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """insert new document in collection

    Args:
        mongo_collection (_pymongo_): _collection object_
    
    Returns:
        _id (_string_): id of document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
