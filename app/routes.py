from flask import Blueprint

hello_world_bp= Blueprint('hello_world', __name__)

@hello_world_bp.route('/hello_world', methods=['GET'])

def hello_world():

    new_hello_world = "Hello, World!"
    return new_hello_world, 200

@hello_world_bp.route('/hello/JSON', methods=['GET'])
def say_hello_json():
    return {
        "name":"TombAnneX", 
        "message":"This is exciting.",
        "hobbies": ["coding", "reading", "word-smithing"]
    }
    new_hobby= "surfing"
    response_bo] + new_hobby
    return response_body