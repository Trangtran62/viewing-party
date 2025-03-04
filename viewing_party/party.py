# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
            }
    
    return None

def add_to_watched(user_data, movie):
    if movie not in user_data.get("watched"):
        user_data.get("watched").append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    if movie not in user_data.get("watchlist"):
        user_data.get("watchlist").append(movie)

    return user_data

def watch_movie(user_data, title):
    movies = user_data.get("watchlist")

    for movie in movies:
        if title == movie["title"]:
            movies.remove(movie)
            user_data.get("watched").append(movie)
    
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = []
    try:
        for movie in user_data["watched"]:
            rating.append(movie["rating"])
        return sum(rating) / len(rating)
    except ZeroDivisionError:
        return 0.0
    except KeyError: # Incase the key watched is missing
        return None

def get_most_watched_genre(user_data):
    genre = {}

    try:
        for movie in user_data["watched"]:
            if movie["genre"] not in genre:
                genre[movie["genre"]] = 1

            genre[movie["genre"]] += 1
            print(genre)
    except KeyError: # Incase the key watched is missing
        return None
    
    if genre:
        return max(genre, key=genre.get)
    
    return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# ------------------------------------------
from frozendict import frozendict

# use frozendict to optimize time complexity, but trade off space
def get_unique_watched(user_data):
    
    friends_watched = []
    friends_watched_set = set()
    watched_set = set()

    for friend in user_data.get("friends"):
        friends_watched.extend(friend.get("watched"))
    
    for movie in friends_watched:
        friends_watched_set.add(frozendict(movie))
        
    for movie in user_data.get("watched"):
        watched_set.add(frozendict(movie))

    return list(watched_set.difference(friends_watched_set))

# use nested loop, less space, more time when data gets big
def get_friends_unique_watched(user_data):
    unique_watched = []
    friends_watched = []
    watched = []

    for movie in user_data.get("watched"):
        watched.append(movie)
        
    for friend in user_data.get("friends"):
        friends_watched.extend(friend.get("watched"))
        
    for movie in friends_watched:
        if movie not in watched and movie not in unique_watched:
            unique_watched.append(movie)

    return unique_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recs = []

    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            recs.append(movie)
    
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    new_rec = []

    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            new_rec.append(movie)
    
    return new_rec

def get_rec_from_favorites(user_data):
    recs = []

    for movie in get_unique_watched(user_data):
        if movie in user_data["favorites"]:
            recs.append(movie)
        
    return recs