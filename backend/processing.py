import gspread as gs

def main():
    gc = gs.service_account(filename='backend/key.json')
    sh1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WkQRziqNg-2dFLd-EDaGIFzWWf8mN6v1lRD9u4JNoWQ/edit?usp=sharing')

    ws1 = sh1.worksheet('Form Responses 1')
    possible = []

    for j in ws1.get_all_records():
        print(j.get("Put the transcript of your conversation here") + ": " + j.get("Upload conversation audio here"))

main()