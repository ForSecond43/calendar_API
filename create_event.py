from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

credentials = pickle.load(open("token_teste.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

#list calendars
calendar_list = service.calendarList().list().execute()
#gets the id of the first calendar
id_calendario = calendar_list ['items'][0]['id']

#Create an event
event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 4103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2021-04-19T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2021-04-19T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 4 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}
event = service.events().insert(calendarId=id_calendario, body=event).execute()