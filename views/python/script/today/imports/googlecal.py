#!/usr/bin/env python3

from __future__ import print_function
import datetime
import os.path
import subprocess
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError
import pathlib

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class GoogleCal:
    def __init__(self):
        pass

    def get_cal_events(self, start_time, end_time):
        current_path = pathlib.Path(__file__).parent
        token_path = current_path.joinpath("json", "token.json")
        cred_path = current_path.joinpath("json", "credentials.json")

        try:
            creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if token_path.exists():
                creds = Credentials.from_authorized_user_file(token_path, SCOPES)
            else:
                token_path.touch()
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        cred_path, SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with token_path.open("w") as token:
                    token.write(creds.to_json())


            service = build('calendar', 'v3', credentials=creds)


#############   ACCESS FIRST CAL, STORE RESULTS IN LIST   ############


            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

            if start_time == "":
                start_time = str(datetime.date.today() - datetime.timedelta(days=1)) + "T23:59:59Z"
            if end_time == "":
                end_time = str(datetime.date.today() + datetime.timedelta(days=6)) + "T23:59:59Z"
            events_result = service.events().list(calendarId='rtl6hms33jcqtotraedlh8l54g@group.calendar.google.com',
                                                  timeMin=start_time,
                                                  timeMax=end_time, singleEvents=True,
                                                  orderBy='startTime').execute()




            returnlist = []
            events = []

            events = events_result.get('items', [])

            for event in events:
                if event['summary'].strip() != "2 thyro":
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    if len(start) > 10:
                        end = start[11:16]
                        start = start[:10] + " " + end

                    returnlist.append((start, event['summary'], "MF"))



    # ##############   ACCESS SECOND CAL, STORE RESULTS IN SAME LIST  #####################

            nowminusone = str(datetime.date.today() - datetime.timedelta(days=1)) + "T23:59:59Z"
            nowplustwo = str(datetime.date.today() + datetime.timedelta(days=2)) + "T23:59:59Z"
            events_result = service.events().list(calendarId='primary', timeMin=start_time,
                                                  timeMax=end_time, singleEvents=True,
                                                  orderBy='startTime').execute()

            events = []
            events = events_result.get('items', [])

            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                if len(start) > 10:
                    end = start[11:16]
                    start = start[:10] + " " + end
                returnlist.append((start, event['summary'], "Pr"))

            return(returnlist)

        except RefreshError:
            token_path.unlink()
            print("Deleted token.json (expired)")
            self.get_cal_events(start_time, end_time)