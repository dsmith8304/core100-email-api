from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "Hello World"

@app.route('/debug', methods=['GET'])
def debug():
    # Log environment details for debugging
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    return {
        "message": "Debug endpoint",
        "working_directory": os.getcwd(),
        "files": os.listdir('.')
    }

application = app
