
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy library to work with databases
import os # Import OS library to interact with the operating system
from flask import Flask # Import Flask framework
import secrets # Import secrets library to generate secure tokens


# initiate flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex() # secret key to enable sessions
# connect the app to the database

path = os.path.join(os.path.dirname(__file__), 'database.db') # to ensure that works on any machine (with any folder setup)
URI = 'sqlite:///{}'.format(path) # Set the URI for the database

app.config['SQLALCHEMY_DATABASE_URI'] = URI # later switch to: #s.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
# Set the application to track modifications to the database
#If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals. 
#source: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
db = SQLAlchemy(app) # Create an instance of the SQLAlchemy database



# import the routing file
from app import routing


#note: GPT assistance was used in adding in line comments