from datetime import datetime
    
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def range_query():
    # You can use datetime(year, month, day) to specify date in the query
    
    print datetime.strptime('2009-1-1','%Y-%m-%d').strftime('%Y-%m-%d')
    query = {'foundingDate': {'$gte' : datetime.strptime('2009-1-1','%Y-%m-%d').strftime('%Y-%m-%d')}}
    return query


if __name__ == "__main__":

    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print "Found cities:", cities.count()
    import pprint
    pprint.pprint(cities[0])
