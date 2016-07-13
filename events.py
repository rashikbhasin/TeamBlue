class Events(object):

    def __init__(self):
        self.event_id=None
        self.name=None
        self.event_info=None
        self.date=None
        self.venue=None
        self.city=None

    def get_name(self):
        return self.name

    def get_info(self):
        return self.event_info

    def get_date(self):
        return self.date

    def get_venue(self):
        return self.venue

    def get_city(self):
        return self.city


class JsonHandler(object):

    def __init__(self):
        self._filename="json_data.json"

    def add_events(self,event):
        pass

    def delete_event(self,event_id):
        pass

    def update_event(self,event_id):
        pass

    def read_event(self,event_id):
        pass

    def upcoming_events(self):
        pass

    def completed_events(self):
        pass

    def search_events_city(self,city):
        pass

    def search_events_date(self,date):
        pass

    def list_events(self,date1,date2):
        pass



class Manager(object):

    def __init__(self):
        self.event=Events()
        self.jsonObj=JsonHandler()


    def add(self):
        pass

    def delete(self,event_id):
        pass

    def update(self,event):
        pass

    def read(self,event_id):
        pass

    def upcoming(self):
        pass

    def completed(self):
        pass

    def search_city(self,city):
        pass

    def search_date(self,date):
        pass

    def list_events(self,date1,date2):
        pass


class Main(object):


    manager=Manager()
    while(True):
        pass
