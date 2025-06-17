from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "Hello World"

@app.route('/debug', methods=['GET'])
def debug():
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    return {
        "message": "Debug endpoint",
        "working_directory": os.getcwd(),
        "files": os.listdir('.')
    }

# Explicitly export for Vercel serverless
if __name__ == '__main__':
    app.run()
application = app
