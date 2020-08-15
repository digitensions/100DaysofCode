#!/usr/bin/env python3

text = open("transcription.txt", "r")
d = {}
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(sorted(d.keys())):
    print(key, ":", d[key])
