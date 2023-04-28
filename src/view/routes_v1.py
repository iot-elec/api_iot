from flask import Blueprint
# from src.controller.v1 import hello

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(hello)
blueprint.route('/get-inventory-details', methods=['GET'])(getInventoryDetails)
