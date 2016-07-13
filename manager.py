from jsonHandler import *
from events import *

class Manager(object):

    def __init__(self):
        self.event = None
        self.jsonObj = JsonHandler()


    def add(self):
        self.event = Events()
        self.event.event_id = raw_input("Enter Event id: ")
        self.event.name = raw_input("Enter Event name: ")
        self.event.event_info = raw_input("Enter Event info: ")
        self.event.date = raw_input("Enter Event date (YYYY-MM-DD): ")
        self.event.venue = raw_input("Enter Event venue: ")
        self.event.city = raw_input("Enter Event city: ")
        self.jsonObj.add_events(self.event)


    def delete(self,event_id):
        self.jsonObj.delete_event(event_id)


    def update(self,event):
        self.jsonObj.update_event(event)

    def read(self,event_id):
        self.jsonObj.read_event(event_id)
        # obj = self.jsonObj.read_event(event_id)
        # print "**********Event data is:**********"
        # print "Event name: ", obj.get_name()
        # print "Event information: ", obj.get_info()
        # print "Event Date: ", obj.get_date()
        # print "Event Venue: ", obj.get_venue()
        # print "Event City: ", obj.get_city

    def upcoming(self):
        self.jsonObj.upcoming_events()

    def completed(self):
        self.jsonObj.completed_events()

    def search_city(self, city):
        self.jsonObj.search_events_city(city)

    def search_date(self, date):
        self.jsonObj.search_events_date(date)

    def list_events(self, date1, date2):
        self.jsonObj.list_events(date1, date2)