import requests
import speech_recognition as sr
from pydub import AudioSegment

def convert_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    file_path_wav = file_path.rsplit('.', 1)[0] + '.wav'
    audio.export(file_path_wav, format="wav")
    return file_path_wav

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

def speech_to_text(file_path):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        return text