#!/usr/bin/env python3
"""Contains a function that inserts a document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document using fields in `kwargs`
    and returns the inserted documents `_id`."""
    return mongo_collection.insert_one(kwargs).inserted_id
