#!/usr/bin/env python3
"""Contains a function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Returns a list of all documents in a collection.
    Returns an empty list if there is no document in the collection"""
    all_students = mongo_collection.find({})
    return list(all_students)
