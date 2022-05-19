import os
from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    statement = 'Hello World!'
    return statement


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port) 
