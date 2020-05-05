import os
if os.path.exists("env.py"):
    import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'ClientTaskManager'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_events')
def get_events():
    return render_template('events.html', events=mongo.db.events.find())


@app.route('/add_event')
def add_event():
    return render_template('addevents.html', users=mongo.db.users.find(), purpose=mongo.db.purpose.find(), status=mongo.db.status.find())


@app.route('/insert_event', methods=['POST'])
def insert_event():
    events = mongo.db.events
    events.insert_one(request.form.to_dict())
    return redirect(url_for('get_events'))


@app.route('/edit_event/<event_id>')
def edit_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    all_users = mongo.db.users.find()
    all_purpose = mongo.db.purpose.find()
    all_status = mongo.db.status.find()
    return render_template('editevent.html', event=the_event, users=all_users, purpose=all_purpose, status=all_status)


@app.route('/update_event/<event_id>', methods=['POST'])
def update_event(event_id):
    mongo.db.events.update(
        {'_id': ObjectId(event_id)},
    {
        'client_name': request.form.get('client_name'),
        'client_ref': request.form.get('client_ref'),
        'location': request.form.get('location'),
        'date': request.form.get('date'),
        'visit_time': request.form.get('visit_time'),
        'pvp_name': request.form.get('pvp_name'),
        'purpose': request.form.get('purpose'),
        'status': request.form.get('status'),
    })
    return redirect(url_for('get_events'))


@app.route('/get_purpose')
def get_purpose():
    return render_template('purpose.html', purpose=mongo.db.purpose.find())


@app.route('/add_purpose')
def add_purpose():
    return render_template('addpurpose.html')


@app.route('/insert_purpose', methods=['POST'])
def insert_purpose():
    purpose = mongo.db.purpose
    purpose.insert_one(request.form.to_dict())
    return redirect(url_for('get_purpose'))


@app.route('/get_users')
def get_users():
    return render_template('users.html', users=mongo.db.users.find())


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)),
            debug=True)
