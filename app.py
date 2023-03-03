from app import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    app.run()

#Make sure your application is correctly binding to the $PORT environment variable. 
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

#heroku logs --app studyabroadcircle 
