#!/usr/bin/env python3

import argparse
import os
import requests

API_URL = "https://api.assemblyai.com/v2/"

def upload_file_to_api(filename):
    '''
    Checks for a valid file then uploads it to Assembly AI so it can be saved to a
    secure URL that only that service can access. Once uploaded the transcription
    API call can be initiated. Returns the API JSON if successful, or None if not.
    '''
    if not os.path.exists('/home/whitej/Desktop/277-django-tips.mp3'):
        return None

    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': os.getenv("ASSEMBLYAI_KEY")}
    response = requests.post("".join([API_URL, "upload"]),  headers=headers,
                             data=read_file(filename))

    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    upload_filename = args.filename
    response_json = upload_file_to_api(upload_filename)
    if not response_json:
        print("That file does not exist")
    else:
        print("File uploaded to URL: {}".format(response_json['upload_url']))
