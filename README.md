🖥️ Automation Scripts Collection

This repository contains 3 small Python utilities that automate different tasks:

1️⃣ auto_git_push.py - Automatic Git Commit and Push

Description:
	•	Continuously monitors a directory (githarkat) for file changes.
	•	After detecting 50 file changes, it automatically:
	•	Stages all changes
	•	Commits with message: “Automatic commit”
	•	Pushes to GitHub

Requirements:
	•	Install dependencies:

pip install gitpython watchdog

	•	Make sure your repo path inside the script is correctly set:

repo_path = '/home/himanshu1009/Desktop/everything_in_here/GITDEMO/githarkat'

	•	Make sure Git credentials are configured for your repo.

Run:

python3 auto_git_push.py


⸻

2️⃣ cleanup.py - Cleanup Unwanted Files

Description:
	•	Compares files inside two folders:
	•	~/Desktop/Temporary/Himanshu
	•	~/Desktop/Temporary/TripImages
	•	Deletes files from TripImages which do not exist (by filename) inside Himanshu.

Use case:
Keep only filtered trip images based on a reference folder.

Run:

python3 cleanup.py

⚠️ Caution: Files will be permanently deleted. Double check before running.

⸻

3️⃣ share_images.py - Google Drive Share Automation

Description:
	•	Uses Google Drive API to automatically share a file/folder with multiple email addresses.

Requirements:
	•	Google Service Account JSON key file.
	•	Enable Google Drive API on Google Cloud Console.
	•	Update:

SERVICE_ACCOUNT_FILE = '/path/to/service_account_key.json'

	•	Install dependencies:

pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2

Run:

python3 share_images.py


⸻

🔧 Global Setup Instructions
	•	Python 3.x
	•	Use virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

You can create requirements.txt file like this:

gitpython
watchdog
google-api-python-client
google-auth
google-auth-oauthlib
google-auth-httplib2


⸻

✅ Optional: Git Preparation before push
	•	You can make a simple .gitignore file to ignore:

*.pyc
__pycache__/
service_account_key.json

	•	Never push your service_account_key.json file to GitHub.

