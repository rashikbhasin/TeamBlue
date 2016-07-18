import json
import datetime
from events import *

class JsonHandler(object):

    def __init__(self):
        self._filename = "json_data.json"


    def add_events(self,event):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        d={event.get_event_id():event.toJson()}
        data.update(d)
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))


    def delete_event(self,event_id):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        del data[event_id]
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))


    def update_event(self,event):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        d=event.toJson()
        data[event.get_event_id()]=d
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))


    def read_event(self,event_id):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        event=Event(event_id,data[event_id]['name'],data[event_id]['info'],data[event_id]['date'],data[event_id]['venue'],data[event_id]['city'])
        return event



    def upcoming_events(self):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        today = str(datetime.date.today())
        lst=[]
        for i in data:
            if data[i]['date'] > today:
                event=Event(i,data[i]['name'],data[i]['info'],data[i]['date'],data[i]['venue'],data[i]['city'])
                lst.append(event)
        return lst


    def completed_events(self):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        today = str(datetime.date.today())
        lst=[]
        for i in data:
            if data[i]['date'] < today:
                event = Event(i,data[i]['name'],data[i]['info'],data[i]['date'],data[i]['venue'],data[i]['city'])
                lst.append(event)
        return lst

    def search_events_city(self,city):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        lst=[]
        for i in data:
            if data[i]['city']==city:
                event = Event(i,data[i]['name'],data[i]['info'],data[i]['date'],data[i]['venue'],data[i]['city'])
                lst.append(event)
        return lst


    def search_events_date(self,date):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        lst=[]
        for i in data:
            if data[i]['date'] == date:
                event = Event(i,data[i]['name'],data[i]['info'],data[i]['date'],data[i]['venue'],data[i]['city'])
                lst.append(event)
        return lst



    def list_events(self,date1,date2):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        lst=[]
        for i in data:
            if data[i]['date'] > date1 and data[i]['date'] < date2:
                event = Event(i,data[i]['name'],data[i]['info'],data[i]['date'],data[i]['venue'],data[i]['city'])
                lst.append(event)
        return lst

