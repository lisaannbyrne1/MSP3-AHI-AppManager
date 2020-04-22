import os
if os.path.exists("env.py"):
    import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'ClientTaskManager'
app.config["MONGO_URI"] = 'mongodb://secret_key = os.environ.get("MONGO_URI")'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_events')
def get_events():
    return render_template('events.html')


@app.route('/add_events')
def add_events():
    return render_template('addevents.html')


@app.route('/edit_events')
def edit_events():
    return render_template('editevents.html')


@app.route('/get_status')
def get_status():
    return render_template('status.html')


@app.route('/edit_status')
def edit_status():
    return render_template('updatestatus.html')


@app.route('/get_purpose')
def get_purpose():
    return render_template('purpose.html')


@app.route('/get_users')
def get_users():
    return render_template('users.html')


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)),
            debug=True)
