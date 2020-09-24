from app.models.event import *


event1 = Event ("oct 19", "Harrisons birthday", 22, "fishbowl", "cake time" )
event2 = Event ("dec 25", "Christmas", 100, "codeclan", "party time")
events = [event1, event2]

def add_new_event(event):
    events.append(event)