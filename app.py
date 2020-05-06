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
    return render_template('add_events.html', users=mongo.db.users.find(), purpose=mongo.db.purpose.find(), status=mongo.db.status.find(), clients=mongo.db.clients.find())


@app.route('/insert_event', methods=['POST'])
def insert_event():
    events = mongo.db.events
    events.insert_one(request.form.to_dict())
    return redirect(url_for('all_events'))


@app.route('/edit_event/<event_id>')
def edit_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    all_clients = mongo.db.clients.find()
    all_users = mongo.db.users.find()
    all_purpose = mongo.db.purpose.find()
    all_status = mongo.db.status.find()
    return render_template('edit_event.html', event=the_event, clients=all_clients, users=all_users, purpose=all_purpose, status=all_status)


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


@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    mongo.db.events.remove({'_id': ObjectId(event_id)})
    return redirect(url_for('all_events'))


"""Purposes"""
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


@app.route('/delete_purpose/<purpose_id>')
def delete_purpose(purpose_id):
    mongo.db.purpose.remove({'_id': ObjectId(purpose_id)})
    return redirect(url_for('purpose'))


@app.route('/edit_purpose/<purpose_id>')
def edit_purpose(purpose_id):
    the_purpose = mongo.db.purpose.find_one({"_id": ObjectId(purpose_id)})
    return render_template('edit_purpose.html', purpose=the_purpose)


@app.route('/update_purpose/<purpose_id>', methods=['POST'])
def update_purpose(purpose_id):
    mongo.db.purpose.update(
        {'_id': ObjectId(purpose_id)},
    {
        'purpose': request.form.get('purpose'),
        'description': request.form.get('description'),
    })
    return redirect(url_for('purpose'))


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


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    return redirect(url_for('users'))


@app.route('/edit_user/<user_id>')
def edit_user(user_id):
    the_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('edit_user.html', user=the_user)


@app.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    mongo.db.users.update(
        {'_id': ObjectId(user_id)},
    {
        'pvp_name': request.form.get('pvp_name'),
        'reg_no': request.form.get('reg_no'),
        'email': request.form.get('email'),
        'company_name': request.form.get('company_name'),
    })
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


@app.route('/delete_client/<client_id>')
def delete_client(client_id):
    mongo.db.clients.remove({'_id': ObjectId(client_id)})
    return redirect(url_for('clients'))


@app.route('/edit_client/<client_id>')
def edit_client(client_id):
    the_client = mongo.db.clients.find_one({"_id": ObjectId(client_id)})
    return render_template('edit_client.html', client=the_client)


@app.route('/update_client/<client_id>', methods=['POST'])
def update_client(client_id):
    mongo.db.clients.update(
        {'_id': ObjectId(client_id)},
    {
        'client_name': request.form.get('client_name'),
        'client_ref': request.form.get('client_ref'),
        'address': request.form.get('address'),
        'email': request.form.get('email'),
    })
    return redirect(url_for('clients'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)),
            debug=True)
