'''
    Dataset: American Movies Scrapped from Wikipedia
    Link: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
    Description: This dataset contains a variety of information about American movies taken from Wikipedia
    Mechanism: using the request library to get the json, then using pymongo to create the database and insert values
'''


import pymongo, json


# connect to the server
connection = pymongo.MongoClient("homer.stuy.edu")
connection.drop_database("goldmanJ-luoE")
print 'database droped'
db = connection[ "goldmanJ-luoE" ]
print 'database added'
collection = db[ "movies" ]
print 'collection added'

# fills the collection with the data
def fill_collection():
    data = json.load( open( 'data/movies.json' ) )
    # fill the collection
    for document in data:
        collection.insert_one( document )


# returns a list of movies with the given title
def by_title(title):
    cursor = collection.find( {"title" : title} )
    movie_list = list()
    for movie in cursor:
        movie_list.append(movie)
    return movie_list


# returns a list of movies made in the given year
def by_year(year):
    cursor = collection.find( {"year" : year} )
    movie_list = list()
    for movie in cursor:
        movie_list.append(movie)
    return movie_list


# returns a list of movies from the given genre
def by_genre(genre):
    cursor = collection.find( {"genre" : genre} )
    movie_list = list()
    for movie in cursor:
        movie_list.append(movie)
    return movie_list


# returns a list of movies made in the given year from the given genre
def by_year_genre(year, genre):
    cursor = collection.find( {"year" : year, "genre" : genre} )
    movie_list = list()
    for movie in cursor:
        movie_list.append(movie)
    return movie_list



# fill the collection for import use
print 'filling the database...'
fill_collection()
print 'collection has been filled'

# ---------------- TESTING ------------------
if( __name__ == '__main__' ):
    print "Searching by title for \"Iron Man\""
    print by_title("Iron Man")
    print "Searching by year for 2012"
    print by_year(2012)
    print "Searching by genre for \"Comedy\""
    print by_genre("Comedy")
    print "Searching by year and genre for 2012 and \"Comedy\""
    print by_year_genre(2012, 'Comedy')
