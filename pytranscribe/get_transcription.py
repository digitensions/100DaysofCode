#!/usr/bin/env python3

import argparse
import os
import requests

API_URL = "https://api.assemblyai.com/v2/"

def get_transcription(transcription_id):
    '''
    Requests the transcript from the API and returns a JSON reponse.
    '''
    endpoint = "".join([API_URL, "transcript/{}".format(transcription_id)])
    headers = {"authorization": os.getenv('ASSEMBLYAI_KEY')}
    response = requests.get(endpoint, headers=headers)
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("transcription_id")
    args = parser.parse_args()
    transcription_id = args.transcription_id
    response_json = get_transcription(transcription_id)
    if response_json['status'] == "completed":
        with open(r'/home/whitej/Desktop/100DaysofCode/pytranscribe/transcription.txt', 'w') as textfile:
            for word in response_json['words']:
                print(word['text'], end=" ", file=textfile)

    else:
        print("Current status of transcription request: {}".format(response_json['status']))

