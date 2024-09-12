import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import email
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

def list_messages(creds, route):
    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me").execute()
        messages = results.get("messages", [])
        if not messages:
            print("no se encontraron mensajes")
            return
        print("Mensajes:")
        for message in messages:
            getMessage(creds, message["id"], route)
    except:
        print(f"An error ocurred: {KeyError}")

def getMessage(credentials, message_id, route):
    # get a message
    try:
        service = build('gmail', 'v1', credentials=credentials)

        # Call the Gmail v1 API, retrieve message data.
        message = service.users().messages().get(userId='me', id=message_id, format='raw').execute()
        # eml content
        mime_msg = email.message_from_bytes(base64.urlsafe_b64decode(message['raw']))
        # Message snippet only.
        print(mime_msg["from"])
        ##print(mime_msg.get_payload())
        #print(mime_msg.as_string())
        name = f"mensaje_{message_id}"
        with open(route + name, 'w') as f:
            f.write(mime_msg)
        
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'A message get error occurred: {error}')

def eml_from_gmail(route):
    main()
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    list_messages(creds, route)
