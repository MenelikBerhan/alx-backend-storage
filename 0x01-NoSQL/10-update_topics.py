#!/usr/bin/env python3
"""Contains a function that updates documents in a collection"""


def update_topics(mongo_collection, name, topics):
    """Updates all documents with `name` in a collection
    by setting strings in `topics` to a field named `topics`."""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
