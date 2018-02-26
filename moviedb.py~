'''
    Dataset: American Movies Scrapped from Wikipedia
    Link: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
    Description: This dataset contains a variety of information about American movies taken from Wikipedia
    Mechanism: using the request library to get the json, then using pymongo to create the database and insert values
'''


import pymongo, json


# create/connect to the database, then create/connect to the collection
connection = pymongo.MongoClient("homer.stuy.edu")
db = connection[ "goldmanJ-luoE" ]
collection = db[ "movies" ]

# fills the collection with the data
def fill_collection():
    data = json.load( open( 'movies.json' ) )
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


# ---------------- TESTING ------------------
fill_collection()
print "Searching by title for \"Iron Man\""
print by_title("Iron Man")
print "Searching by year for 2012"
print by_year(2012)
print "Searching by genre for \"Comedy\""
print by_genre("Comedy")
print "Searching by year and genre for 2012 and \"Comedy\""
print by_year_genre(2012, 'Comedy')
