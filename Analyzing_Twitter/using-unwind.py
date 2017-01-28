
#!/usr/bin/env python

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = []
    unwind = { "$unwind" : "$isPartOf"}
    pipeline.append(unwind)
    match = { "$match" : { "country" : "India" } }
    pipeline.append(match)
    group = {
        "$group" :  {
                        "_id" : "$isPartOf",
                        "count" : { "$sum" : 1 } 
                    }
    }
    pipeline.append(group)
    sort = { "$sort" : { "count" : -1 } }
    pipeline.append(sort)
    limit = { "$limit" : 1 }
    pipeline.append(limit)
    print pipeline
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    for document in result:
        print document
