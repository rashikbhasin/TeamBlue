class Events(object):

    def __init__(self):
        self._event_id=None
        self._name=None
        self._event_info=None
        self._date=None
        self._venue=None
        self._city=None

    def get_event_id(self):
        return self._event_id

    def get_name(self):
        return self._name

    def get_info(self):
        return self._event_info

    def get_date(self):
        return self._date

    def get_venue(self):
        return self._venue

    def get_city(self):
        return self._city

    def set_event_id(self,event_id):
        self._event_id = event_id

    def set_name(self,name):
        self._name=name

    def set_info(self,info):
        self._event_info=info

    def set_date(self,date):
        self._date=date

    def set_venue(self,venue):
        self._venue=venue

    def set_city(self,city):
        self._city=city