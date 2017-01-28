#!/usr/bin/env python
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [ ]
    dict = {
            "$match" :  {
                            "user.time_zone" : "Brasilia",
                            "user.statuses_count" : {"$gte" : 100}
                        }   
        }
    pipeline.append(dict)
    dict = {
            "$project" :    {
                                "followers" : "$user.followers_count",
                                "screen_name" : "$user.screen_name",
                                "tweets" : "$user.statuses_count"
                            }
        }
    pipeline.append(dict)
    dict = {
            "$sort" : { "followers" : -1}
        }
    pipeline.append(dict)
    dict = { "$limit" : 1}    
    pipeline.append(dict)    
    return pipeline

def aggregate(db, pipeline):
    result = db.tweets.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    for document in result:
        print document
