from flask import Flask
import json
import os

app = Flask(__name__)

# --- Test Block: Load, find, and access a field ---
test_report = ""
try:
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, '..', 'Core100EmailLibrary.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        emails = json.load(f)

    test_report += f"SUCCESS: JSON loaded with {len(emails)} records. "

    match = next((e for e in emails if e.get("email_id") == "2.2"), None)

    if match:
        test_report += "SUCCESS: Found a match for email_id '2.2'. "

        # --- New Test Logic ---
        try:
            subject = match.get('subject')
            if subject:
                test_report += f"SUCCESS: Accessed subject field: '{subject}'"
            else:
                test_report += "FAILURE: 'subject' field exists but is empty."
        except Exception as e_field:
            test_report += f"FAILURE: Could not access 'subject' field. Error: {e_field}"
        # --- End of New Test Logic ---

    else:
        test_report += "FAILURE: Could not find a match for email_id '2.2'."

except Exception as e:
    test_report = f"FAILURE: An exception occurred. Error: {e}"
# --- End of Test Block ---


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return test_report
