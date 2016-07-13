import json
import datetime

class JsonHandler(object):

    def __init__(self):
        self._filename = "json_data.json"


    def add_events(self,event):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        data['event_id'].append(int(event.get_event_id()))
        data['name'].append(event.get_name())
        data['event_info'].append(event.get_info())
        data['date'].append(event.get_date())
        data['venue'].append(event.get_venue())
        data['city'].append(event.get_city())
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))
        changed.close()


    def delete_event(self,event_id):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        index=data['event_id'].index(int(event_id))
        del data['event_id'][index]
        del data['name'][index]
        del data['event_info'][index]
        del data['date'][index]
        del data['venue'][index]
        del data['city'][index]
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))
        changed.close()


    def update_event(self,event):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        index = data['event_id'].index(int(event.get_event_id()))
        data['event_id'][index]=event.get_event_id()
        data['name'][index] = event.get_name()
        data['event_info'][index] = event.get_info()
        data['date'][index] = event.get_date()
        data['venue'][index] = event.get_venue()
        data['city'][index] = event.get_city()
        with open(self._filename,'w+') as changed:
            changed.write(json.dumps(data,indent=4))
        changed.close()


    def read_event(self,event_id):
        data = None
        with open(self._filename,'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        index = data['event_id'].index(int(event_id))
        print "**********Event Details are:**********"
        self.print_details(data,index)



    def print_details(self,data,index):
        print "Event Name: ", data['name'][index]
        print "Event Info: ", data['event_info'][index]
        print "Event City: ", data['date'][index]
        print "Event Venue: ", data['venue'][index]
        print "Event City: ", data['city'][index]
        print "***************************************"


    def upcoming_events(self):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        today = str(datetime.date.today())
        count=0
        print "**********Upcoming Events are:**********"
        for e_date in data['date']:
            if e_date > today:
                print "***************************************"
                self.print_details(data,count)
            count+=1


    def completed_events(self):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        today = str(datetime.date.today())
        count = 0
        print "**********Completed Events are:**********"
        for e_date in data['date']:
            if e_date < today:
                print "***************************************"
                self.print_details(data, count)
            count += 1

    def search_events_city(self,city):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        count = 0
        print "**********Events in this City are:**********"
        for e_city in data['city']:
            if e_city==city:
                print "***************************************"
                self.print_details(data, count)
            count+=1


    def search_events_date(self,date):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        count = 0
        print "**********Events on this day are:**********"
        for e_date in data['date']:
            if e_date == date:
                print "***************************************"
                self.print_details(data, count)
            count += 1


    def list_events(self,date1,date2):
        data = None
        with open(self._filename, 'r') as data_file:
            data = json.load(data_file)
        data_file.close()
        count = 0
        print "**********Events between these dates are:**********"
        for e_date in data['date']:
            if e_date > date1 and e_date < date2:
                print "***************************************"
                self.print_details(data, count)
            count += 1
