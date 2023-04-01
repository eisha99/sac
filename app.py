# Import necessary libraries
import os
from app import app
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

if __name__ == '__main__': # Define the entry point of the application
    #app.run()
    port = int(os.environ.get('PORT', 5000)) # Get the port number from the environment variable or use 5000 as the default
    app.run(host='0.0.0.0', port=port) 
    # Run the Flask application on all available network interfaces and the specified port




#heroku logs --app studyabroadcircle 
