from flask import Blueprint

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        
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
@hello_world_bp.route('/broken-endpoint-with-broken-server-code', methods=['GET'])
    
def broken_endpoint():
    response_body = {
        "name":"Ada Lovelace", 
        "message":"Hello.",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby= "surfing"
    response_body. append(new_hobby)
    return response_body