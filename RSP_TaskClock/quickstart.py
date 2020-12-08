from __future__ import print_function
from datetime import datetime
import pytz
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def getEvents():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])

    return events 

def getNextEvt():
    events = getEvents()
    nextEvt = events[0]
    return nextEvt

def eventGoingOn(event):
    """
    parameter: next event
    return: True if start time of next event past now(); False otherwise.  
    """
    now = datetime.now().timestamp()
    evtStart = datetime.strptime(event['start'].get('dateTime'), "%Y-%m-%dT%H:%M:%S%z").timestamp()
    
    tdiff = now - evtStart

    if tdiff < 0: 
        print("no current event")
        return False
    else:
        print("event going on")
        return True

def getEvtTitle(event):
    evtTitle = event['summary']
    return evtTitle

def getEvtNotes(event):
    evtNotes = event['description']
    return evtNotes

def getEvtStartTime(event):
    """
    return: datetime object of start time of a given event  
    """
    start = event['start'].get('dateTime')
    stTimeOb = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z")
    return stTimeOb

def getEvtEndTime(event):
    """
    return: datetime object of end time of a given event  
    """
    end = event['end'].get('dateTime')
    endTimeOb = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S%z")
    return endTimeOb

def getStEndTimeText(stTimeOb, endTimeOb):
    """
    return: a string that contains start and end time information of a given event  
    """
    stTime = stTimeOb.strftime("%I:%M %p")
    endTime = endTimeOb.strftime("%I:%M %p")

    timeInfo = stTime + " to " + endTime + "."
    return timeInfo

def calHrMnDiff(time_1, time_2):
    """
    parameter: two datetime objects between which time difference is to calculated
    return: (days, hours, minutes), a tuple of time difference in days, hours and minutes 
    limitation: time difference should not exceed over a year
    """
    tdiff = (time_2 - time_1 + datetime.min).timetuple()
    return (tdiff[2] - 1, tdiff[3], tdiff[4]) #datetime.min adds MINYEAR, 1 month and 1 day


def getEndCtDn(eventEndTime):
    now = datetime.now(pytz.utc)
    diffDays, diffHrs, diffMins = calHrMnDiff(now, eventEndTime)
    return getHrMinCtDn(diffDays, diffHrs, diffMins)


def getHrMinCtDn(days, hours, minutes):
    cdDays = ""
    cdHours = ""
    cdMins = ""

    if days > 0:
        cdDays = str(days) + " days "
    if hours > 0:
        cdHours = str(hours) + " hours "
    if minutes > 0:
        cdMins = str(minutes) + " minutes"
    else:
        cdMins = "0 minutes" 

    return cdDays + cdHours + cdMins

def getFolEvt():
    """
    return: the following event after the current one
    """
    events = getEvents()
    nextEvt = events[1]
    return nextEvt


def getFolEvtCtDn(followingEvt):
    startob = getEvtStartTime(followingEvt)
    now = datetime.now(pytz.utc)
    diffDays, diffHrs, diffMins = calHrMnDiff(now, startob)
    return getHrMinCtDn(diffDays, diffHrs, diffMins)


if __name__ == '__main__':
    # main()
    nextEvt = getNextEvt()

    if eventGoingOn(nextEvt): 
        currEvt = nextEvt

        currEvtTitle = getEvtTitle(currEvt)
        print("event title: " + currEvtTitle)

        stTimeOb = getEvtStartTime(currEvt)
        endTimeOb = getEvtEndTime(currEvt)

        currEvtTimeInfo = getStEndTimeText(stTimeOb, endTimeOb)
        print("event time: " + currEvtTimeInfo)

        currEvtCountDown = getEndCtDn(endTimeOb)
        print("event end in: " + currEvtCountDown)
        
        currEvtNotes = getEvtNotes(currEvt)
        print("event notes: " + currEvtNotes)

        folEvt = getFolEvt()
        print("following event: " + getEvtTitle(folEvt))

        folEvtStartIn = getFolEvtCtDn(folEvt)
        print("following event start in: " + folEvtStartIn + ".")

    else: 
        restInfo1 = "Rest period." 
        restInfo2 = "No task." 
        print(restInfo1 + '\n' + restInfo2)

