from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

#Get Token
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("teste.json", scopes=scopes)
credentials = flow.run_console()

#Save credentials to a file in order to be able to access it later
pickle.dump(credentials, open("token_teste.pkl", "wb"))
