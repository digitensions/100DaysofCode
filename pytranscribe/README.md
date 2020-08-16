You can try running this code by using my personal ASSEMBLYAI account API token and upload/transcript UIs:
You don't need to run upload_audio_file.py unless you want to try another MP3 transcription.

Run this in your venv before running any of the AssemblyAI scripts:
`export ASSEMBLYAI_KEY=3536b3aba82942d3b427c310a9672e49`

To run another transcription of episode 277 of Talk Python To Me, use:
`python3 initiate_transcription.py 7aa20292-0c84-4593-ad0b-32391987265b`

To download the get_transcription, create a transcription.txt file and change the path in the script, then run:
`python3 get_transcription.py g1nw0m0qs-ce85-4d25-8a6f-96786f0eed88`

I made a quick word_sort_count.py script that sorts the results into words. I'd prefer a filter for highest word occurrences listed first,
so I'll maybe update this in days to come.

Please be kind if you use my AssemblyAI details.
The full tutorial is available here: https://www.fullstackpython.com/blog/transcribe-recordings-speech-text-assemblyai.html
It doesn't have the export to .txt feature, but just prints to console.
