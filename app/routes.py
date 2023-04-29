from flask import Blueprint, jsonify    

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Lord of the It Depends", "A fantasy novel set Philadelphia"),
#     Book(2, "2023: A Depends Odyssey", "A science fiction novel set in Seattle"),
#     Book(3, "Did the Butler Do It? It Depends", "A mystery novel set in the 1920s"),
#     Book(4, "Do You Love Me? It Depends", "A romance novel set New York City"),
# ]
        
hello_world_bp= Blueprint('hello_world', __name__)
books_bp = Blueprint("books", __name__, url_prefix="/books") 

@books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description,
#             })
#     return jsonify(books_response)
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book_id = int(book_id)
#     for book in books:
#         if book.id == book_id:
#             return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description,
#          }
    

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
    response_body.append(new_hobby)
    return response_body