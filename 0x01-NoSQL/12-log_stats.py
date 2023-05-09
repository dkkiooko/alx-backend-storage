#!/usr/bin/env python3
""" stats aboutn nginx logs stores in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    """ get stats using a variety of mentods """

    # get client and connect to db and collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # count number of documents in collection
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    # mehtods
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        # count number of documents with each method
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')
    
    # status check no of docs with get method and status path
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')
