from flask import Blueprint, jsonify, make_response, request

from app import db
from app.models.books import Book

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
        
books_bp = Blueprint("books", __name__, url_prefix="/books") 

@books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])
    db.session.add(new_book)
    db.session.commit()
    return make_response(f"Book {new_book.title} successfully created", 201)


# @books_bp.route("", methods=["GET"])
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
    