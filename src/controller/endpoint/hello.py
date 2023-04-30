from src.model.redis import cache

def greet():
    return "Hello world"

def hello():
    cache.incr('hits')
    counter = str(cache.get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"




# def getMetadata():
#     # from src.model.dbmodel.inventory_model import InventoryModel
#     # from src.model.dbmodel.item_model import ItemModel
#     # it = ItemModel()