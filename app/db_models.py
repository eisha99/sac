
#importing libraries
from sqlalchemy import Enum
from app import db

class User(db.Model): #we begin by defining a User class that inherits from db.Model.
    """
    This is a class for User (table) with the columns password and username respectively 
    """
    __tablename__ = 'users' # Define the __tablename__ attribute to specify the name of the database table.
    username = db.Column(db.String(50), primary_key = True) # Define the username column with a max char of 50
    password = db.Column(db.String, nullable  = False) # # Define the password column with no maximum length and set it as not nullable. nullable prevents from having empty inputs

# Initialize database 
db.create_all()
db.session.commit()