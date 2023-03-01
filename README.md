
# Kanban Board

## Functionality

This is web applicatoin with a kanban board; every task can be in one of three states: to-do, done, doing. The board the divided into three columns, each marked with a step in the respective working state. Each user has their own kanban board and can create new tasks, move tasks to different states, or delete the tasks. Users can sign up, log in and log out.

## File Structure

The root directory contains the following files:

- `test.py` contains the unittests.
- `requirements.txt` contains the required packages for the project.
- `app.py` gets the app to run.
- .env includes env variables that need to be set

The `app` folder contains the application files:

- `__init__.py` contains the configuration and initializes the app.
- `routing.py` contains routes which serves frontend pages made up of HTML and CSS.
- `db_models.py` connects to the database and contains the SQLAlchemy tables.
- `templates/` is a folder which contains html templates to be rendered.

This is based on [this structure](http://flask.pocoo.org/docs/0.12/patterns/packages).

## Installation

Start virtual environment

    $ python -m venv venv
    $ source venv/bin/activate

Install necessary dependencies

    $ pip install -r requirements.txt

Start flask server (from the root directory)

    $ python app.py

Your Kanban board should be up and running at http://127.0.0.1:5000/

## Unit Testing

On the project root directory, run

    $ python3 -m unittest discover test


## Resources
The following resources were referenced:

- https://semantic-ui.com/ -- used for styling 

- https://flask.palletsprojects.com/en/2.0.x/tutorial/