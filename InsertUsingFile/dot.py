def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def dot_query():
    query = {"width" : {"$gt" : 2.5}}
    return query


if __name__ == "__main__":

    db = get_db()
    query = dot_query()
    cars = db.autos.find(query)

    print "Found cars:", cars.count()
    import pprint
    pprint.pprint(cars[0])
