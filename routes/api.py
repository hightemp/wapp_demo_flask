from flask import Blueprint

from ..extensions import db
# from ..models.book import Book
# from ..models.category import Category
# from ..models.author import Author

api = Blueprint('api', __name__)

# @api.route("/api/books/<sID>")
# def api_get_book(sID):
#     return { 'book': Book.query.filter_by(id=sID).first() }