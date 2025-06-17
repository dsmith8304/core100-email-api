# Core100 Email API

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fdsmith8304%2Fcore100-email-library-js)

A serverless API deployed on Vercel that serves email data for the CapsimCore experience.

## ✨ Tech Stack

* **Node.js**: The JavaScript runtime environment.
* **Vercel**: For Serverless Functions and global deployment.
* **GitHub Codespaces**: For the cloud-based development environment.

## 📁 Final Project Structure

The project uses a co-located data and logic structure within the `api` directory, which is a Vercel convention.

.
├── api/
│   ├── email-data.js   # The email data, exported as a JS module.
│   └── email.js        # The serverless function API endpoint.
├── package.json        # Project metadata.
└── README.md           # This file.


## 🚀 API Endpoint

The API exposes a single endpoint to retrieve email details by ID.

### Production URL

`https://core100-email-library-js.vercel.app/api/email`

### Query Parameter

* `email_id` (string): The ID of the email to fetch (e.g., `2.1`).

### Example Request

```bash
curl "[https://core100-email-library-js.vercel.app/api/email?email_id=2.1](https://core100-email-library-js.vercel.app/api/email?email_id=2.1)"
💻 Development
This project is developed using GitHub Codespaces.

To start developing, launch a new codespace from the repository's main page.
All tools (Node.js, Git) are pre-configured in the environment.
Edit the files (api/email-data.js to change data, api/email.js to change logic).
Commit and push changes via the integrated Source Control panel or the terminal.
☁️ Deployment
Deployment is handled automatically by Vercel's integration with GitHub. Any git push to the main branch will trigger a new production deployment.


