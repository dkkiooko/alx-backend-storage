#!/usr/bin/env python3
""" list schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """returns list of schools having specific topic

    Args:
        mongo_collection (_pymongo_): _collection object_
        topic (_string_): _topic to be searched_
    """
    return list(mongo_collection.find({'topics':topic}))
