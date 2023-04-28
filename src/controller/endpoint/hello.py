from src.model.redis import cache

def greet():
    return "Hello world"

def hello():
    cache.incr('hits')
    counter = str(cache.get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"