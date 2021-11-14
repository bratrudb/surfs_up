#Import Flask and create instance
from flask import Flask
app = Flask(__name__)

# Starting point of route
@app.route('/')
def hello_world():
    return 'Hello world'