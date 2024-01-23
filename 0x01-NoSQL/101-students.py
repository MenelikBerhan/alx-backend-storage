#!/usr/bin/env python3
"""Contains a function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted in descending order by average score.The
    average score will be part of each item, with key `averageScore`"""
    return mongo_collection.aggregate([
            {'$project': {'name': 1,
                          'averageScore': {'$avg': "$topics.score"}}},
            {'$sort': {'averageScore': -1}}
        ])

    # or using unwind and group
    # return mongo_collection.aggregate(
    #     [
    #         {'$unwind': "$topics"},
    #         {'$group': {'_id': "$_id", 'name': {'$first': '$name'},
    #                     'averageScore': {'$avg': "$topics.score"}}},
    #         {'$sort': {'averageScore': -1}}
    #     ])
