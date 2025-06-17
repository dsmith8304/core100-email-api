from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# --- Proven, Working JSON Loading Block ---
try:
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, '..', 'Core100EmailLibrary.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        emails = json.load(f)
except Exception as e:
    emails = []
    print(f"CRITICAL ERROR LOADING JSON: {e}")

# --- The Main API Endpoint with a HARD-CODED test ---
@app.route('/email', methods=['GET'])
def get_email_by_id():
    # The original line that reads from the URL is commented out.
    # email_id = request.args.get('email_id')
    
    # As you suggested, we supply the email_id directly to test the logic.
    email_id = "2.2" 
    
    if not emails:
        return jsonify({"error": "Email data could not be loaded. Check server logs."}), 500

    match = next((e for e in emails if e.get("email_id") == email_id), None)
    
    if match:
        # If the lookup succeeds, return the actual JSON data for email 2.2
        return jsonify(match)
    else:
        return jsonify({"error": f"No email found with hard-coded ID {email_id}."}), 404

# --- The Status Check Endpoint ---
@app.route('/status', methods=['GET'])
def home():
    if not emails:
        return "Flask API is running, but FAILED to load email data."
    return f"Flask API is running and email data is loaded with {len(emails)} records."
