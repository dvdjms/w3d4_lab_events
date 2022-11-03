from models.event import *
import datetime

event1 = Event(datetime.date(2022, 11, 17), "Fireworks Night", 32, "Park", "Fun night out at local community park", "Recurring")
event2 = Event(datetime.date(2022, 12, 22), "Knitting Club", 8, "30 Waverley Street", "Learn Knitting with Brenda", "Not recurring")
events = [event1, event2]

def add_new_event(event):
    events.append(event)

