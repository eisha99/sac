
# Study Abroad Circle

## Functionality

This is a website for "Study Abroad Circle", a platform where users can get more information about studying abroad, finding opportunities and guides (resources in the form of videos, blogs etc). The website has a welcome page which allows users to log in and log out. Then they have the options of exploring different pages namely home, resources, opportunities, chats and mentorship.

## File Structure

These files are in the directory:

- `test.py` used to store the unit tests for the web application.
- `requirements.txt` used to store a list of the required packages for the project.
- `app.py` defines the main Flask application 
- .env includes env variables that need to be set

The `app` folder contains the application files:

- `__init__.py` defines the initialization code for the package. 
- `routing.py` contains routes which serves frontend pages made up of HTML and CSS.
- `db_models.py` defines the SQL connection for the web-app
- `templates/` folder which has all the html templates that are to be rendered.

This is based on [this structure](http://flask.pocoo.org/docs/0.12/patterns/packages).

## Installation

Start virtual environment

    $ python3 -m venv venv
    $ source venv/bin/activate

Install necessary dependencies

    $ pip3 install -r requirements.txt

Start flask server (from the root directory)

    $ python app.py

the website should run at http://127.0.0.1:5000/

## Unit Testing

On the project root directory, run

    $ python3 -m unittest discover test


## Resources

The following resources were used in the creation of this web app:

- https://semantic-ui.com/ -- this was used for styling purposes

- https://flask.palletsprojects.com/en/2.0.x/tutorial/

- https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/

- https://www.youtube.com/watch?v=QAFL-QOuejk&ab_channel=MayanwolfeStreams

- https://github.com/vuhcl/kanban-board

- Chat GPT -- used to assist in bug fixing, adding inline comments and fixing tests  

- DialogFlow and Kommunicative were used in 1) building an AI chatbot 2) integrating chatbot into Flask app
