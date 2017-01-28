#!/usr/bin/env python
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = []
    pipeline.append(
        { "$group" : { "_id" : "$source",
                       "count" : { "$sum" : 1} } })
    pipeline.append({ "$sort" : { "count" : -1 } })
    return pipeline

def tweet_sources(db, pipeline):
    result = db.tweets.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = tweet_sources(db, pipeline)
    for document in result:
        print(document)


