from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Path to your service account key file (JSON file)
SERVICE_ACCOUNT_FILE = '/Users/hanshubharti/Desktop/Projects/config/service_account_key.json'

# Define the required scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate with the service account
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

def share_file(file_id, email):
    """
    Share a file on Google Drive with a specific email address.
    :param file_id: The ID of the Google Drive file or folder to share.
    :param email: The email address to grant access.
    """
    try:
        # Define the permission
        permission = {
            'type': 'user',  # Can also be 'group' or 'domain'
            'role': 'reader',  # Can also be 'writer' or 'commenter'
            'emailAddress': email
        }
        
        # Share the file
        drive_service.permissions().create(
            fileId=file_id,
            body=permission,
            fields='id'
        ).execute()

        print(f"File shared with {email}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the file ID of your Google Drive file or folder
    file_id = "17BB5Cz3i401ekTBFknG0FUMK1URLE2ts"

    # Replace with the list of email addresses you want to share with
    email_list = [
        "sssnehaad12@gmail.com",
        "shrutibastakoti15@gmail.com",
        "kashishbhandari676@gmail.com"
    ]

    for email in email_list:
        share_file(file_id, email)