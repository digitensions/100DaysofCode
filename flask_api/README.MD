### To use these API scripts you will need to install Python3 and Flask.

### python api_local.py
Navigate to this address using a browser once the script is running:
## 127.0.0.1:5000/api/v1/resources/books/all
This script calls on a script dictionary of my current reading materials (don't judge me)!
You can separately view each dictionary entry (displayed in JSON) by using ?id=1:
## 127.0.0.1:5000/api/v1/resources/books?id=1

### python api_database.py
This script needs the database.db file in the same directory alongside it.
Again you can navigate to the following link (don't try to run these two script together):
## 127.0.0.1:5000/api/v1/resources/books/all
In addition you can set queries using the dictionary IDs:
## 127.0.0.1:5000/api/v1/resources/books?publication=2010
## 127.0.0.1:5000/api/v1/resources/books?author=China Mieville

These scripts were written with the help of this amazing resource:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
