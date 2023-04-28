from flask import Blueprint
from src.controller.endpoint.hello import hello, greet

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/hello', methods=['GET'])(hello)
blueprint.route('/', methods=['GET'])(greet)
