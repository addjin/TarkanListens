# This code is largely based on the sample code provided by Google API. For the original version;
#   https://developers.google.com/gmail/api/quickstart/python
#   https://github.com/googleworkspace/python-samples/blob/main/gmail/quickstart/quickstart.py

import os.path
import util
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = util.readLinesToList('scopes.txt')

def getGmailService():
    creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)

        creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        # results = service.users().labels().list(userId="me").execute()
        # labels = results.get("labels", [])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")
  
    return service


def getMessages(service, labelIds):
    """Returns a list of emails with the specified labels."""
    messageIdsDict = service.users().messages().list(userId='me', labelIds=labelIds).execute()

    if len(messageIdsDict) == 0:
        return []
    
    messageIds = [msg['id'] for msg in messageIdsDict]


def getUnreadMessages(service):
    """Returns all unread emails."""
    return getMessages(service=service, labelIds=['UNREAD'])
