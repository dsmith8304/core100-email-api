from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load email data once at startup
json_path = os.path.join(os.path.dirname(__file__), 'Core100EmailLibrary.json')
with open(json_path, 'r') as f:
    emails = json.load(f)

@app.route('/email')
def get_email_by_id():
    email_id = request.args.get('email_id')
    if not email_id:
        return jsonify({"error": "Please provide an email_id param."}), 400

    match = next((e for e in emails if e.get("email_id") == email_id), None)
    if match:
        return jsonify(match)
    else:
        return jsonify({"error": f"No email found with ID {email_id}."}), 404
