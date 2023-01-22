from ..extensions import db
from sqlalchemy import *
from wtforms_alchemy import ModelForm, ModelFormField
from sqlalchemy.orm import *

class Category(db.Model):
    id = Column(Integer, primary_key=True)
    name = db.Column(String(50))
    parent_id = db.Column(Integer, ForeignKey("category.id"))
    children = relationship("Category", backref=backref("parent", remote_side=[id]))
    books = relationship("Book", backref=backref("category", remote_side=[id]))

class CategoryForm(ModelForm):
    class Meta:
        model = Category