#!/usr/bin/env python3
""" change all topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """change all topics of a document based on name

    Args:
        mongo_collection (_pymongo_): _collection object_
        name (_string_): _school name to update_
        topics (_list of strings_): _list of topics to be approached_
    """
    filter = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(filter, new_values)
