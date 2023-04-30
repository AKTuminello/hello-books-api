from flask import Blueprint, jsonify    

from app import db
from app.models.books import Book, jsonify, make_response, request


books_bp = Blueprint("books_bp", __name__, url_prefix="/books") 

@books_bp.route("", methods=["GET"])
def read_all_books():
    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description,
            })
    return jsonify(books_response)

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])
    db.session.add(new_book)
    db.session.commit()
    
    return f"Book {new_book.title} successfully created", 201

