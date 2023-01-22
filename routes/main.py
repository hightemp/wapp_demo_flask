from flask import Blueprint

from ..extensions import db
# from ..models.book import Book
# from ..models.category import Category
# from ..models.author import Author
from ..baselib import render_template

main = Blueprint('main', __name__)

@main.route("/")
def root():
    return "<h1>root</h1>"

# @main.route("/books/edit/<sID>")
# def edit_book(sID):
#     Book.query.filter_by(id=sID).first()
#     render_template("books/edit.html")