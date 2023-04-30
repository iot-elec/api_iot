import sys
from flask import Flask, request, jsonify
from src.controller.utils import str_to_list_int

from src.model.dbmodel.model import InventoryModel, ItemModel

from src.controller.database.database import SessionLocal
import logging

# {
# 			"inventoryId": [18, 78, 75, 4, 144, 0],
# 			"itemModel": {
# 				"itemID": 1,
# 				"itemName": "Mature Cheddar Cheese 400G",
# 				"productDescription": {
# 					"details": "Mature Cheddar cheese.100% British milk.\\n Hand selected cheese for a strong and full flavour",
# 					"size": 400,
# 					"unitSize": "G"
# 				},
# 				"allergyInformation": "Contains milk"
# 			},
# 			"exp": "2023-04-25",
# 			"mfg": "2023-04-09",
# 			"price": 6.02,
# 			"priceUnit": "GBP"
# 		}



def get_inventory_details(card_id: str):
    session = SessionLocal()
    print(card_id, file=sys.stderr)
    card_id_list = str_to_list_int(card_id)
    print(card_id_list, file=sys.stderr)


    if (card_id_list == -1):
        return jsonify({}), 400
    else:
		

        inventory_joined = session.query(InventoryModel, ItemModel).join(InventoryModel, ItemModel.id == InventoryModel.itemModelId).filter(InventoryModel.inventoryId ==str(card_id_list) ).first()
        res = {
			"inventoryId": inventory_joined.InventoryModel.inventoryId,
			"itemModel": {
				"itemID": inventory_joined.ItemModel.id,
				"itemName": inventory_joined.ItemModel.itemName,
				"productDescription": {
					"details": inventory_joined.ItemModel.details,
					"size": inventory_joined.ItemModel.size,
					"unitSize": inventory_joined.ItemModel.unitSize
				},
				"allergyInformation": inventory_joined.ItemModel.allergyInformation
			},
			"exp": inventory_joined.InventoryModel.expire,
			"mfg": inventory_joined.InventoryModel.manufacturing,
			"price": inventory_joined.InventoryModel.price,
			"priceUnit": inventory_joined.InventoryModel.priceUnit
		}
        return jsonify(res), 200

def pay():
    # print(request.body)
    pass
