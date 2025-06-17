from flask import Flask
import json
import os

app = Flask(__name__)

# --- Test Block: Load the JSON and then try to find one record ---
test_report = ""
try:
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, '..', 'Core100EmailLibrary.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        emails = json.load(f)

    test_report += f"SUCCESS: JSON loaded with {len(emails)} records. "

    # --- New Test Logic ---
    match = next((e for e in emails if e.get("email_id") == "2.2"), None)

    if match:
        test_report += "SUCCESS: Found a match for email_id '2.2'."
    else:
        test_report += "FAILURE: Could not find a match for email_id '2.2'."
    # --- End of New Test Logic ---

except Exception as e:
    test_report = f"FAILURE: An exception occurred. Error: {e}"
# --- End of Test Block ---


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return test_report
