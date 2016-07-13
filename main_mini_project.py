from manager import *
import sys
from events import *


class Main(object):

    manager = Manager()
    while(True):
        print "Enter 1.Add Event 2.Delete Event 3.Update Event 4.Read Event 5.Upcoming Event 6.Completed Event 7.Search By City 8.Search By Date 9.List Events 10.Exit"
        input = int(raw_input())
        if input == 1:
            manager.add()
        elif input == 2:
            event_id = raw_input("Enter Event id to be deleted: ")
            manager.delete(event_id)
        elif input == 3:
            event = Events()
            event.event_id = raw_input("Enter Event id to be updated: ")
            event.name = raw_input("Enter Event new name: ")
            event.event_info = raw_input("Enter Event new info: ")
            event.date = raw_input("Enter Event new date (YYYY-MM-DD): ")
            event.venue = raw_input("Enter Event new venue: ")
            event.city = raw_input("Enter Event new city: ")
            manager.update(event)
        elif input == 4:
            event_id = raw_input("Enter Event Id: ")
            manager.read(event_id)
        elif input == 5:
            manager.upcoming()
        elif input == 6:
            manager.completed()
        elif input == 7:
            city = raw_input("Enter city name: ")
            manager.search_city(city)
        elif input == 8:
            date = raw_input("Enter particular date: ")
            manager.search_date(date)
        elif input==9:
            date1 = raw_input("Enter date 1: ")
            date2 = raw_input("Enter date 2: ")
            manager.list_events(date1,date2)
        else:
            sys.exit()

if __name__ == "__main__":
    Main()
