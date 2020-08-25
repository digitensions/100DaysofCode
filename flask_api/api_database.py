import flask
from flask import request, jsonify
import sqlite3

# Initialise the Flash DEBUG configuration
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Configures data as a dictionary in col[0]/row[idx]
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

# Using sqlite3 to import data from books.db and set to GET path below. Return as JSON file.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory  # Uses function to return items as dictionaries, not lists
    cur = conn.cursor()  # Cursor object moves through database to pull out data 
    all_books = cur.execute('SELECT * FROM books;').fetchall()  # Execute sql query, for * (all) book data

    return jsonify(all_books) # Convert all book variable to JSON output

# Handles exceptions where incorrect query is given
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# Configures three filtering options, id - published - author
@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()

