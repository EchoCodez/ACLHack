from processing import classify_message
import gspread as gs

gc = gs.service_account(filename='backend/key.json')
sh1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WkQRziqNg-2dFLd-EDaGIFzWWf8mN6v1lRD9u4JNoWQ/edit?usp=sharing')

ws1 = sh1.worksheet('Form Responses 1')

def get_data():
    for i in ws1.get_all_records():
        result = classify_message(i.get("Put the transcript of your conversation here"))
        print(f'The message "{i.get("Put the transcript of your conversation here")}" is classified as: {result}')

get_data()

