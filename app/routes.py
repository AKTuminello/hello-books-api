from app import db
from app.models.books import Book
from flask import Blueprint, jsonify, make_response, request, abort

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

@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return make_response("", 404)
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
    }

