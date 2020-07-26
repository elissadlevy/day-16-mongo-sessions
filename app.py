# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:moninananM4!@cluster0-qezhz.mongodb.net/database?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    collection = mongo.db.events
    events = collection.find({})
    return render_template('index.html', events=events)

# CONNECT TO DB, ADD DATA

@app.route('/newevent', methods = ['GET', 'POST'])
def new_event():
    if request.method == 'GET':
        return render_template('new_event.html')
    else:
        # collect data from the new_event.html form 
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        user_name = request.form['user_name']

        # insert data into database
        collection = mongo.db.events
        collection.insert({"event":event_name, "date":event_date, "user": user_name})
     
        return "Data added.  Go to <a href='/index'>home</a>."
