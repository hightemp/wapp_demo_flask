from ..extensions import db
from sqlalchemy import *
from wtforms_alchemy import ModelForm, ModelFormField
from sqlalchemy.orm import *

class Author(db.Model):
    id = db.Column(Integer, autoincrement=True, primary_key=True)
    fio = db.Column(String(255), nullable=False)
    books = relationship("Book", backref=backref("authors", remote_side=[id]))

class AuthorForm(ModelForm):
    class Meta:
        model = Author