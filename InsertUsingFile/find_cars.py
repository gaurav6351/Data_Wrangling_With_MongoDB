def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def in_query():
    # Write the query
    query = {'manufacturer_label' : 'Ford Motor Company','assembly_label':{'$in': ['Germany', 'United Kingdom', 'Japan']}}
    
    return query


if __name__ == "__main__":

    db = get_db()
    query = in_query()
    autos = db.autos.find(query, {"name":1, "manufacturer":1, "assembly": 1, "_id":0})

    print "Found autos:", autos.count()
    import pprint
    for a in autos:
        pprint.pprint(a)
