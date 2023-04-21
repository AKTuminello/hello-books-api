from flask import Blueprint

hello_world_bp= Blueprint('hello_world', __name__)

@hello_world_bp.route('/hello_world', methods=['GET'])

def hello_world():

    new_hello_world = "Hello, World!"
    return new_hello_world, 200