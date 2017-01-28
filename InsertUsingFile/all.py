def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def in_query():
    # Write the query
    query = {'modelYears' :{'$in': [1965,1966,1967,1968,1969]}}
    
    return query


if __name__ == "__main__":

    db = get_db()
    query = in_query()
    autos = db.autos.find(query, {"name":1, "manufacturer":1, "modelYears": 1, "_id":0})

    print "Found autos:", autos.count()
    import pprint
    for a in autos:
        pprint.pprint(a)
