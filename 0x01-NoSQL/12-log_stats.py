#!/usr/bin/env python3
"""a Python script that provides some stats about
Nginx logs stored in `nginx` collection in `logs` MongoDB."""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # number of all logs
    print('{} logs'.format(collection.count_documents({})))

    # number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print('\tmethod {}: {}'.format(
            method, collection.count_documents({'method': method})))

    # number of logs for `GET` method with `/status` path
    print('{} status check'.format(
        collection.count_documents({'method': 'GET', 'path': '/status'})
    ))
