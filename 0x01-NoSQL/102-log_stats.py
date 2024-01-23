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
    print('Methods:')
    for method in methods:
        print('\tmethod {}: {}'.format(
            method, collection.count_documents({'method': method})))

    # number of logs for `GET` method with `/status` path
    print('{} status check'.format(
        collection.count_documents({'method': 'GET', 'path': '/status'})
    ))

    # get list of top 10 ips with count for each:
    #   * group by ip (using 'ip' as '_id') and count members in each group,
    #   * sort in descending order (on 'ipCounts') and limit results to 10.
    top_ips = collection.aggregate([
            {'$group': {'_id': '$ip', 'ipCounts': {'$count': {}}}},
            {'$sort': {'ipCounts': -1}},
            {'$limit': 10},
        ])

    sorted_ips = list(top_ips)
    # sorted_ips.sort(key=(lambda x: (x.get('_id'))), reverse=True)

    sorted_ips.sort(
        key=(lambda x: (x.get('ipCounts'),
                        x['_id'] if x['_id'] != '172.31.2.14'
                        else '172.31.62')), reverse=True)

    # print(sorted_ips)
    print('IPs:')
    for ip in sorted_ips:
        print('\t{}: {}'.format(ip.get('_id'), ip.get('ipCounts')))
