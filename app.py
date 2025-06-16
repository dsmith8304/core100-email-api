from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# --- FIX IS HERE ---
# Load the email data from the JSON file into a variable called 'emails'
try:
    with open('Core100EmailLibrary.json', 'r') as f:
        emails = json.load(f)
except FileNotFoundError:
    emails = [] # Or handle the error as you see fit if the file might be missing

# This is your API endpoint
@app.route('/api/email', methods=['GET'])
def get_email_by_id():
    email_id = request.args.get('email_id')
    if not email_id:
        return jsonify({"error": "Please provide an email_id parameter."}), 400

    match = next((e for e in emails if e.get("email_id") == email_id), None)
    
    if match:
        return jsonify(match)
    else:
        return jsonify({"error": f"No email found with ID {email_id}."}), 404

# A default route to check if the server is running
@app.route('/', methods=['GET'])
def home():
    return "Flask API is running."
