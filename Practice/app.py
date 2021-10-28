#Import the Flask Dependency
from flask import Flask

#Create a new flask app instance
app = Flask(__name__)

#Create Flask routes
@app.route('/')
def hello_world():
    return 'Hello world'