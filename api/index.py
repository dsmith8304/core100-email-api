from flask import Flask
import json
import os

app = Flask(__name__)

# --- Test Block: Try to load the JSON file ---
file_load_status = ""
try:
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, '..', 'Core100EmailLibrary.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        emails = json.load(f)
    # If we get here, the file was found and parsed successfully.
    file_load_status = f"SUCCESS: Core100EmailLibrary.json was found and loaded. It contains {len(emails)} records."
except Exception as e:
    # If anything goes wrong during file open or JSON parsing, catch the error.
    file_load_status = f"FAILURE: Could not load JSON file. Error: {e}"
# --- End of Test Block ---


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # This function will now report the status of our file loading test.
    return file_load_status
