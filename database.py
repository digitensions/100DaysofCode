#!/usr/bin/env python3

import mysql.connector

'''
A short script that connects to training database and access Dictionary table
Import mysql.connector very problematic in Linux and MacOS.
Only successful way found to pip install into VENV on MacOs and run from within the VENV.
Made it user interactive so it asks for a word to be supplied before information returned.
'''

con = mysql.connector.connect(                      # Training connection info available
    user = "user",
    password = "password",
    host = "0.0.0.0",
    database = "database01"
)
cursor = con.cursor()

def main():
    word = str(input("\nPlease enter your own word: "))
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    results = cursor.fetchall()

    if results:
        for result in results:
            answer = result[1]
        print("The word you have chosen '{0}' has the following definitions: {1}".format(word, answer))
    else:
        print("Sorry, your word is not found")

if __name__ == "__main__":
    main()
