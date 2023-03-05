import os
from app import app
from dotenv import load_dotenv

from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('static', path)

load_dotenv()

if __name__ == '__main__':
    #app.run()
    #Make sure your application is correctly binding to the $PORT environment variable. 
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



#heroku logs --app studyabroadcircle 
