from processing import classify_message
import gspread as gs
import time
from send_email import send_email
from conversion import download_file_from_google_drive, convert_audio, speech_to_text

gc = gs.service_account(filename='backend/key.json')
sh1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WkQRziqNg-2dFLd-EDaGIFzWWf8mN6v1lRD9u4JNoWQ/edit?usp=sharing')

ws1 = sh1.worksheet('Form Responses 1')


def stot(path):
    download_file_from_google_drive(path, 'destination_filename.wav')
    file_path_wav = convert_audio('destination_filename.wav')
    text = speech_to_text(file_path_wav)
    return text


def get_data(body):
    data = ws1.get_all_records()[-1].get("Put the transcript of your conversation here")
    for i in stot(data[data.index("="):]).split("."):
        result = classify_message(i)
        if result == "Fraudulent":
            body += (f'The message "{i}" is classified as: {result}\n')
    for j in str(ws1.get_all_records()[-1].get("Upload conversation audio here")).split("."):
        result = classify_message(i)
        if result == "Fraudulent":
            body += (f'The speech "{j}" is classified as: {result}\n')
    return body

thing = ws1.get_all_records()[-1].get("Put the transcript of your conversation here")

while True:
    body = ""
    time.sleep(1)
    if ws1.get_all_records()[-1].get("Put the transcript of your conversation here") != thing:
        full = get_data(body)
        send_email("Fraudulent Conversation Notice", full, ws1.get_all_records()[-1].get("Enter your email address. You will receive the analyzation report at this email."))
        thing = ws1.get_all_records()[-1].get("Put the transcript of your conversation here")

