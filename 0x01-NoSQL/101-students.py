#!/usr/bin/env python3
""" sort by average score """


def top_students(mongo_collection):
    """sort by average score

    Args:
        mongo_collection (_pymongo_): _collection object_
    Return:
        all students sorted by average
    """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top_student
