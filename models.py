'''PyCODE | @_py.code'''

# ? Importing Libraries
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# ! DB init
db = SQLAlchemy()

# | Snippet Database Model
class Snippet(db.Model):
    __tablename__ = "snippet"
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)
    lang = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)