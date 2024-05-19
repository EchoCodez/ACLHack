from processing import classify_message
import gspread as gs
import time

gc = gs.service_account(filename='backend/key.json')
sh1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WkQRziqNg-2dFLd-EDaGIFzWWf8mN6v1lRD9u4JNoWQ/edit?usp=sharing')

ws1 = sh1.worksheet('Form Responses 1')

def get_data():
    for i in str(ws1.get_all_records()[-1].get("Put the transcript of your conversation here")).split("."):
        result = classify_message(i)
        if result == "Fraudulent":
            print(f'The message "{i}" is classified as: {result}')

thing = ws1.get_all_records()[-1].get("Put the transcript of your conversation here")

while True:
    time.sleep(1)
    if ws1.get_all_records()[-1].get("Put the transcript of your conversation here") != thing:
        get_data()
        thing = ws1.get_all_records()[-1].get("Put the transcript of your conversation here")

