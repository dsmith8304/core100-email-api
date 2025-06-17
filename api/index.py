from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# --- FINAL CORRECTED LOADING ---
try:
    # Get the absolute path of the directory where this script is running
    script_dir = os.path.dirname(__file__) 
    # Construct the path to the JSON file, which is now in the parent directory
    json_path = os.path.join(script_dir, '..', 'Core100EmailLibrary.json')

    with open(json_path, 'r', encoding='utf-8') as f:
        emails = json.load(f)
except FileNotFoundError:
    # This case is for when the file doesn't exist at all.
    emails = []
    print("ERROR: Core100EmailLibrary.json not found.")

except json.JSONDecodeError as e:
    # This will catch syntax errors in the JSON file and print the exact error.
    emails = []
    print("--- CRITICAL: JSON DECODING FAILED ---")
    print(f"The file 'Core100EmailLibrary.json' could not be parsed.")
    print(f"Error Message: {e}")
    print("-----------------------------------------")


# This is your API endpoint
@app.route('/email', methods=['GET'])
def get_email_by_id():
    email_id = request.args.get('email_id')
    if not email_id:
        return jsonify({"error": "Please provide an email_id parameter."}), 400

    if not emails:
        # This handles the case where the JSON failed to load
        return jsonify({"error": "Email data could not be loaded. Check server logs."}), 500

    match = next((e for e in emails if e.get("email_id") == email_id), None)
    
    if match:
        return jsonify(match)
    else:
        return jsonify({"error": f"No email found with ID {email_id}."}), 404

# A default route to check if the server is running
@app.route('/', methods=['GET'])
def home():
    if not emails:
        return "Flask API is running, but FAILED to load email data."
    return "Flask API is running and email data is loaded."
