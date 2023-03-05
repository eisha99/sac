
from sqlalchemy import Enum
from app import db

class User(db.Model):
    """
        Creates a user table. 
    """
    __tablename__ = 'users'
    username = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String, nullable  = False) # nullable prevents from having empty inputs

# Initialize database 
db.create_all()
db.session.commit()