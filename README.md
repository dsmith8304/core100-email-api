# core100-email-api
Fetches email descriptions for Caprai from Core100EmailLibrary.json.
This is a lightweight Flask-based API that serves CapsimCore Inbox emails from a structured JSON file.

## 🔍 What It Does

This API exposes a single endpoint:

Where `x.y` is the ID of a specific email (e.g., `1.1`, `2.3`, etc.) as defined in the `Core100EmailLibrary.json` file.

The API returns the full email object, including character, introduction, response type, and options—designed for deterministic lookup from a GPT or other front-end.

## 📁 Files

- `Core100EmailLibrary.json` — Structured data source for all Core100 emails.
- `app.py` — Flask server code to load and serve the email data.

## 🧪 Sample Request

```bash
curl "http://localhost:5000/email?email_id=1.1"

{
  "email_id": "1.1",
  "character": "Andrew Grove",
  "introduction": "Welcome to the company, CEO. We have big shoes to fill.",
  "response_type": "multiple_choice",
  "response_options": [
    "Thank you, I'm ready.",
    "Let's get to work.",
    "I'm nervous but excited."
  ]
}
