from flask import render_template, request # ADDED
from app import app
from models.event_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    
    event_name = request.form['name']
    event_guests = request.form['guest_number']
    event_location = request.form['room_location']
    event_description = request.form['description']
    event_date = request.form['date']
    try:
        event_recurring = request.form['recurring']
        print(event_recurring)
        recurring = "Recurring"
    except:
        recurring = "Not recurring"

    new_event = Event(event_date, event_name, event_guests, event_location, event_description, recurring)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)



