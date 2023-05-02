import sys
from flask import Flask, request, jsonify
from sqlalchemy import JSON
from src.controller.utils import convert_date_format, str_to_list_int

from src.model.dbmodel.model import InventoryModel, ItemModel

from src.controller.database.database import SessionLocal

def get_inventory_details(card_id: str):
    session = SessionLocal()
    card_id_list = str_to_list_int(card_id)

	# TODO: read from cache insted of DB

    if (card_id_list == -1):
        return jsonify({}), 400
    else:
		

        inventory_joined = session.query(InventoryModel, ItemModel).join(InventoryModel, ItemModel.id == InventoryModel.itemModelId).filter(InventoryModel.isBuy == False).filter(InventoryModel.inventoryId ==str(card_id_list) ).first()
        res = {
			"inventoryId": str_to_list_int(inventory_joined.InventoryModel.inventoryId),
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
			"exp": convert_date_format(inventory_joined.InventoryModel.expire),
			"mfg": convert_date_format(inventory_joined.InventoryModel.manufacturing),
			"price": inventory_joined.InventoryModel.price,
			"priceUnit": inventory_joined.InventoryModel.priceUnit
		}
        
        session.close()
        return jsonify(res), 200

'''body is the list of Id
{
    "id": [
        [1,23,55],[1,23,44]
	]
}
'''
def pay(json: JSON):
	session = SessionLocal()
	id_list = json['id']
	for id in id_list:
		if (type(id) == list):
			continue
		id = str(str_to_list_int(id))

	try:
		session.query(InventoryModel)\
    	            .filter(InventoryModel.inventoryId.in_(id_list))\
    	            .update({InventoryModel.isBuy: True})
		session.commit()
		return jsonify({}), 200
	except:
		session.rollback()
		return jsonify({}), 400
	finally:
	    session.close()
        
	
		
             
    

