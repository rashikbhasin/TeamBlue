class Events(object):

    def __init__(self):
        self._event_id=None
        self._name=None
        self._event_info=None
        self._date=None
        self._venue=None
        self._city=None

    def get_event_id(self):
        return self.event_id

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