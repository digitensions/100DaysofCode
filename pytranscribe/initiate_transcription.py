#!/usr/bin/env python3

import argparse
import os
import requests

API_URL = "https://api.assemblyai.com/v2/"
CDN_URL = "https://cdn.assemblyai.com/"

def initiate_transcription(file_id):
    '''
    Sends request to API to transcribe file uploaded to API. This will not immediately
    return a transcript as it takes time to analyse and perform. Next function retrieves.
    '''
    endpoint = "".join([API_URL, "transcript"])
    json = {"audio_url": "".join([CDN_URL, "upload/{}".format(file_id)])}
    headers = {
        "authorization": os.getenv("ASSEMBLYAI_KEY"),
        "content_type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_id")
    args = parser.parse_args()
    file_id = args.file_id
    response_json = initiate_transcription(file_id)
    print(response_json)
