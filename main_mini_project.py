from Manager import *
import sys
from events import *


class Main(object):

    def printing(evnt):
        st = evnt.get_event_id()
        print "Event id :", st
        st = evnt.get_name()
        print "Event Name :", st
        st = evnt.get_info()
        print "Event info :", st
        st = evnt.get_date()
        print "Event date :", st
        st = evnt.get_venue()
        print "Event venue :", st
        st = evnt.get_city()
        print "Event City :", st

    manager = Manager()
    while(True):
        print "Enter 1.Add Event 2.Delete Event 3.Update Event 4.Read Event 5.Upcoming Event 6.Completed Event 7.Search By City 8.Search By Date 9.List Events 10.Exit"
        input = int(raw_input())
        if input == 1:
            event=Events()
            st=raw_input("Enter event id :")
            event.set_event_id(st)
            st = raw_input("Enter event name :")
            event.set_name(st)
            st = raw_input("Enter event info :")
            event.set_info(st)
            st = raw_input("Enter event date :(YYYY-MM-DD)")
            event.set_date(st)
            st = raw_input("Enter event venue :")
            event.set_venue(st)
            st = raw_input("Enter event city :")
            event.set_city(st)
            manager.add(event)
        elif input == 2:
            event_id = raw_input("Enter Event id to be deleted: ")
            manager.delete(event_id)
        elif input == 3:
            event = Events()
            st1 = raw_input("Enter event id to be updated:")
            event.set_event_id(st1)
            st = raw_input("Enter  event name for Update :")
            event.set_name(st)
            st = raw_input("Enter event info for Update:")
            event.set_info(st)
            st = raw_input("Enter event date for Update:(YYYY-MM-DD)")
            event.set_date(st)
            st = raw_input("Enter event venue for Update:")
            event.set_venue(st)
            st = raw_input("Enter event city for Update:")
            event.set_city(st)
            manager.update(event)
            print "Event Information is SuccessFully Updated For Event id",st1
        elif input == 4:
            event_id = raw_input("Enter Event Id: ")
            event=manager.read(event_id)
            print "Event Information For Event id :",event_id
            printing(event)

        elif input == 5:
            event=manager.upcoming()
            print "Upcoming Events :"
            for i in event:
                printing(i)

        elif input == 6:
            event=manager.completed()
            print "Completed Events :"
            for i in event:
                printing(i)
        elif input == 7:
            city = raw_input("Enter city name: ")
            event_city=manager.search_city(city)
            print "Events in  ",city
            for i in event_city:
                printing(i)
        elif input == 8:
            date = raw_input("Enter Particular Date: (YYYY-MM-DD) ")
            event_date=manager.search_date(date)
            print "Events On :",date
            for i in event_date:
                printing(i)
        elif input==9:
            date1 = raw_input("Enter date 1:(YYYY-MM-DD) ")
            date2 = raw_input("Enter date 2:(YYYY-MM-DD) ")
            event_list_between_date=manager.list_events(date1,date2)
            print "Events Between ",date1," and ", date2
            for i in event_list_between_date:
                printing(i)
        else:
            sys.exit()



if __name__ == "__main__":
    Main()
