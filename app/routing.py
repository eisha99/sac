
from flask_sqlalchemy import SQLAlchemy
import os 
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from app import db,app
from app.db_models import User
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
def index():
    """ 
        Main page of the web application. Handles cases when the user is logged in and when they are not. 
    """
    # check if logged in, i.e. if the session has a saved username
    # not session.get('username')
    if 'username' not in session:
        return render_template('welcome.html')
    # else:
    #     # create three lists, each of each type of task
    #     #to_do, doing, done = [],[],[]
    #     # retrieve data for the user with given username from the database
    #     tasks = db.session.query(Task).filter(Task.username==session.get('username'))
        # for task in tasks:
        #     if task.status == 'to_do':
        #         to_do.append(task)
        #     elif task.status == 'doing':
        #         doing.append(task)
        #     else:
        #         done.append(task)
    #return render_template("index.html", to_do = to_do, doing =doing, done=done, user=session.get('username'))

# TODO add encryption for the password
@app.route('/signup', methods=["GET","POST"])
def sign_up():
    """ 
        Sign up pages. has get and post methods
    """
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username==request.form['username']).first()
        if not user:
            user = User(username = request.form['username'], password = request.form['password'])
            db.session.add(user)
            db.session.commit()
            #flash('User created!')
            session['username'] = user.username
            flash('Login successful')
            return redirect(url_for('index'))
        else:
            flash('Please, choose a different username. This one is already taken')
            return render_template("signup.html")
    else:
        return render_template("signup.html")

@app.route('/login', methods = ['GET','POST'])
def login(): 
    """ 
        Login page. It has get and post methods. Dispslays error message if incorrect login data provided.
    """
    error = None
    # authenticate the user
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username==request.form['username']).first()
        if not user:
            flash('Invalid username!')
            
            error = 'Invalid username/password'
            # no need to redirect bc already on login page
        elif user.password == request.form['password']:
            # log in
            app.logger.info(session['username'])
            session['username'] = user.username
            app.logger.info(session['username'])
            #flash('Login successful')
            return redirect(url_for("index"))
        else:
            flash('Incorrect password!')
            error = 'Invalid username/password'

    return render_template("login.html", error = error)

@app.route('/logout')
def log_out():
    """
        User log out
    """
    # Remove the username from the session
    session.pop('username', None)
    #flash('Logged out successfully!')
    return redirect(url_for('index'))

@app.route('/resources')
def resources():
    """ 
     This is the resources page, it redirects users to Youtube videos and application guides.
    """
    return render_template('resources.html') 

@app.route('/mentorship')
def mentorship():
    """ 
     This is the mentorship page where users can sign up for a mentee or mentor position.
    """
    return render_template('mentorship.html') 


@app.route('/chats')
def chats():
    """ 
     This is the chats page where studwent can access our Whatsapp and Telegram channels.
    """
    return render_template('chats.html') 

@app.route('/opportunities')
def opportunities():
    """ 
     This is where we will link our expert chat system that redirects students to the most suitable scholarship opportunities
    """
    return render_template('opportunities.html') 

if __name__ == '__main__':
    app.run(debug=True)


