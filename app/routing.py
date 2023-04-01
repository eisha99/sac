
from flask_sqlalchemy import SQLAlchemy
import os 
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from app import db,app
from app.db_models import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import send_from_directory, request
import json


@app.route('/')
def index():
    """ 
        This is the home page for the web app
    """
    #since a new user is "not" logged in
    if 'username' not in session:
        return render_template('welcome.html') #without login
        #the user is directed straight to the home page
    else:
        return render_template("index.html") #with login
    # user=session.get('username')) 

    

# TODO add encryption for the password
@app.route('/signup', methods=["GET","POST"])
def sign_up():
    """ 
        This is the sign up page where users can enter an email and a password to create an account.
    """
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username==request.form['username']).first()
        if not user:
            user = User(username = request.form['username'], password = request.form['password'])
            #user is asked to enter a username and a password
            db.session.add(user) #for the current session we add this user
            db.session.commit()
            #flash('User created!')
            session['username'] = user.username 
            #the username for this session then becomes this username
            flash('Login successful')
            return redirect(url_for('index'))
        else:
            flash('The username you entered is already taken. Please choose a different one.')
            return render_template("signup.html")
    else:
        return render_template("signup.html")
    
    #comments

@app.route('/login', methods = ['GET','POST'])
def login(): 
    """ 
        This is the Log In page where users can login with their existing username and password
    """
    error = None
    # authenticate the user
    if request.method == 'POST': #we first check if the user's username and password match database records
        user = db.session.query(User).filter(User.username==request.form['username']).first()
        if not user: #if the username isn't correct
            flash('Username is invalid')
            error = 'Incorrect email/password combination'
            # no need to redirect bc already on login page
        elif user.password == request.form['password']:
            # log in
            #app.logger.info(session['username'])
            session['username'] = user.username
            app.logger.info(session['username'])
            #flash('Login successful')
            return redirect(url_for("index"))
        else:
            flash('Password is invalid')
            error = 'Incorrect email/password combination'

    return render_template("login.html", error = error)

@app.route('/logout')
def log_out():
    """
        This is used in the case where a logged in users wishes to log out
    """
    #we pop the username from the session
    session.pop('username', None)
    #flash('Logged out successfully!')
    return redirect(url_for('index')) #user is redirected to the index which takes it to the home page

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

@app.route("/kommunicate")
def kommunicate():
    return """
    <script type="text/javascript">
        (function(d, m){
            var kommunicateSettings = 
                {"appId":"2be0ffe1cd81d18a72b4bd02814f1ac42","popupWidget":true,"automaticChatOpenOnNavigation":true};
            var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
            s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
            var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
            window.kommunicate = m; m._globals = kommunicateSettings;
        })(document, window.kommunicate || {});
    </script>
    """

@app.route('/opportunities')
def opportunities():
    """ 
     This is where we will link our expert chat system that redirects students to the most suitable scholarship opportunities
    """
    # return render_template('opportunities.html')
    return render_template('opportunities.html', kommunicate=True)



if __name__ == '__main__':
    app.run(debug=True)


