#!/usr/bin/env python3
"""Contains a function that find documents based on topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns documents in a collection having a `topic`
    in their `topics` field."""
    return list(mongo_collection.find({'topics': topic}))
