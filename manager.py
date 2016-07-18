from jsonHandler import *
from events import *

class Manager(object):

    def __init__(self):
         pass

    def add(self,event):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        d = {event.get_event_id(): event.toJson()}
        data.update(d)
        with open(self._filename, 'w+') as changed:
            changed.write(json.dumps(data, indent=4))


    def delete(self,event_id):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        del data[event_id]
        with open(self._filename, 'w+') as changed:
            changed.write(json.dumps(data, indent=4))

    def update(self,event):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        d = event.toJson()
        data[event.get_event_id()] = d
        with open(self._filename, 'w+') as changed:
            changed.write(json.dumps(data, indent=4))
    def read(self,event_id):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        event = Event(event_id, data[event_id]['name'], data[event_id]['info'], data[event_id]['date'],
                      data[event_id]['venue'], data[event_id]['city'])
        return event


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

   
