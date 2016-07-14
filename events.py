class Event(object):

    def __init__(self,event_id,name,event_info,date,venue,city):
        self._event_id=event_id
        self._name=name
        self._event_info=event_info
        self._date=date
        self._venue=venue
        self._city=city

    def toJson(self):
        d={"name":self.get_name(),"info":self.get_info(),"date":self.get_date(),"venue":self.get_venue(),"city":self.get_city()}
        return d

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

    # def set_event_id(self,event_id):
    #     self._event_id = event_id
    #
    # def set_name(self,name):
    #     self._name=name
    #
    # def set_info(self,info):
    #     self._event_info=info
    #
    # def set_date(self,date):
    #     self._date=date
    #
    # def set_venue(self,venue):
    #     self._venue=venue
    #
    # def set_city(self,city):
    #     self._city=city