from app import app
from flask import render_template, request, redirect
from app.models.events_list import events, add_new_event
from app.models.event import *


@app.route('/')
def index():
    # return "hello"
    return render_template("index.html", title= "Home", events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
    event_date= request.form["date"]
    event_name_of_event = request.form["name_of_event"]
    event_num_of_guest = request.form["num_of_guest"]
    event_room_location = request.form["room_location"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name_of_event, num_of_guest, room_location, description)
    add_new_event (new_event)

    return redirect('/')