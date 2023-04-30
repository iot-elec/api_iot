from flask import Blueprint
from flask import Flask, request, jsonify

from src.controller.endpoint.v1 import get_inventory_details, pay


blueprint_v1 = Blueprint('blueprint_v1', __name__)

@blueprint_v1.route('/get-inventory-details/<card_id>', methods=['GET'])
def v1_get_inventory_details(card_id):
    return get_inventory_details(card_id)

@blueprint_v1.route('/checkout', methods=['POST'])
def v1_checkout():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return pay(json)
    else:
        return 'Content-Type not supported!', 400