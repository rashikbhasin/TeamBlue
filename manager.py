from jsonHandler import *
from events import *

class Manager(object):

    def __init__(self):
         pass

    def add(self,event):
        jsonObj = JsonHandler()
        jsonObj.add_events(event)


    def delete(self,event_id):
        jsonObj=JsonHandler()
        jsonObj.delete_event(event_id)


    def update(self,event):
        jsonObj = JsonHandler()
        jsonObj.update_event(event)

    def read(self,event_id):
        jsonObj = JsonHandler()
        return jsonObj.read_event(event_id)

    def upcoming(self):
        jsonObj = JsonHandler()
        return jsonObj.upcoming_events()

    def completed(self):
        jsonObj = JsonHandler()
        return jsonObj.completed_events()

    def search_city(self, city):
        jsonObj = JsonHandler()
        return jsonObj.search_events_city(city)

    def search_date(self, date):
        jsonObj = JsonHandler()
        return jsonObj.search_events_date(date)

    def list_events(self, date1, date2):
        jsonObj = JsonHandler()
        return jsonObj.list_events(date1, date2)
