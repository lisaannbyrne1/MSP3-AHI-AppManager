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


"""Appointments"""
@app.route('/')
@app.route('/all_events')
def all_events():
    return render_template('all_events.html', events=mongo.db.events.find())


@app.route('/add_event')
def add_event():
    return render_template('add_events.html', users=mongo.db.users.find(), purpose=mongo.db.purpose.find(), status=mongo.db.status.find())


@app.route('/insert_event', methods=['POST'])
def insert_event():
    events = mongo.db.events
    events.insert_one(request.form.to_dict())
    return redirect(url_for('all_events'))


@app.route('/edit_event/<event_id>')
def edit_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    all_users = mongo.db.users.find()
    all_purpose = mongo.db.purpose.find()
    all_status = mongo.db.status.find()
    return render_template('edit_event.html', event=the_event, users=all_users, purpose=all_purpose, status=all_status)


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
    return redirect(url_for('all_events'))


"""Appointment Purposes"""
@app.route('/purpose')
def purpose():
    return render_template('purpose.html', purpose=mongo.db.purpose.find())


@app.route('/add_purpose')
def add_purpose():
    return render_template('add_purpose.html')


@app.route('/insert_purpose', methods=['POST'])
def insert_purpose():
    purpose = mongo.db.purpose
    purpose.insert_one(request.form.to_dict())
    return redirect(url_for('get_purpose'))


"""Vet users"""
@app.route('/users')
def users():
    return render_template('users.html', users=mongo.db.users.find())


@app.route('/add_user')
def add_user():
    return render_template('add_user.html')


@app.route('/insert_user', methods=['POST'])
def insert_user():
    users = mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for('users'))


"""Clients"""
@app.route('/clients')
def clients():
    return render_template('clients.html', clients=mongo.db.clients.find())


@app.route('/add_client')
def add_client():
    return render_template('add_client.html')


@app.route('/insert_client', methods=['POST'])
def insert_client():
    clients = mongo.db.clients
    clients.insert_one(request.form.to_dict())
    return redirect(url_for('clients'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)),
            debug=True)
