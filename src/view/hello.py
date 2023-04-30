from flask import Blueprint
from src.controller.endpoint.hello import hello, greet

blueprint_hello = Blueprint('blueprint_hello', __name__)

blueprint_hello.route('/hello', methods=['GET'])(hello)
blueprint_hello.route('/', methods=['GET'])(greet)
