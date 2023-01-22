from ..extensions import db
from sqlalchemy import *
from wtforms_alchemy import ModelForm, ModelFormField

class Book(db.Model):
    id = Column(Integer, primary_key=True)
    name = db.Column(String(255))
    author_id = db.Column(Integer, ForeignKey("author.id"))
    year = db.Column(String(255))
    category_id = db.Column(Integer, ForeignKey("category.id"))

class BookForm(ModelForm):
    class Meta:
        model = Book