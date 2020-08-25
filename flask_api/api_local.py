import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalogue in the form of list of dictionaries.

books = [
    {'id': 0,
    'title': 'A Fire Upon the Deep',
    'author': 'Vernor Vinge',
    'first_sentence': 'The cold sleep iteself was dreamless.',
    'year_published': '1992'},
    {'id': 1,
    'title': 'Ted Talks',
    'author': 'Chris Anderson',
    'first_sentence': 'The house lights dim.',
    'year_published': '2016'},
    {'id': 2,
    'title': 'The Luminaries',
    'author': 'Eleanor Catton',
    'first_sentence': 'The twelve men congregated in the smoking room of the Crown Hotel gave the impression of a party accidentally met.',
    'year_published': '2014'},
    {'id': 3,
    'title': 'Women Who Fly',
    'author': 'Serenity Young',
    'first_sentence': "Perhaps the world's most famous image of a winged female is the statue of the Greek goddess of victory, Nike, also known as the Victory of Samothrace - a centrepiecee of the Louvre Museum, where it is magnificently displayed in all its glory at the top of Daru stairway, formerly the museum's main entrance.",
    'year_published': '2018'},
    {'id': 4,
    'title': 'Jonathan Strange and Mr Norrell',
    'author': 'Susanna Clarke',
    'first_sentence': 'Some years ago there was in the city of York a society of magicians.',
    'year_published': '2004'},
    {'id': 5,
    'title': 'Titus Groan',
    'author': 'Mervyn Peake',
    'first_sentence': 'Gormenghast, that is, the main massing of the original stone, taken by itself would have displayed a certain ponderous architectural quality were it possible to have ignored the circumfusion of those mean dwellings that swarmed like an epidemic around its outer walls',
    'year_published': '1968'},
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>'''

# A route to return all of the available entries in our catalogue.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    '''
    Check if an ID was provided as part of URL
    If ID there assign to variable
    If no ID, display an error message
    '''
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No ID provided. Please specify"

    # Create list to populate
    results = []

    '''
    Loop through data and match results that fit the requested ID.
    IDs are unique, but other fields might return many results.
    '''
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use jsonify function from Flask to convert list of dictionaries to JSON
    return jsonify(results)    


app.run()
