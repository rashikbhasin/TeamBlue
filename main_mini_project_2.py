from manager import *
import sys
from events import *

from flask import Flask, render_template, request,jsonify,json
import json

app = Flask(__name__)

manager = Manager()

@app.route("/add",methods=["POST","GET"])
def add_event():
    #if request.method=="POST":
        headers = {'Content-Type': 'application/json'}
        # print "HELLO u are at added"
        d=request.json
        # print d
        event=Event(d["event_id"],d["name"],d["event_info"],d["date"],d["venue"],d["city"])
        #event=Event("3","aamya","info 3","2016-07-08","venue 3","mumbai")
        manager.add(event)
        # x={"Added":"Successful"}
        x={"event_id":d["event_id"],"name":d["name"],"event_info":d["event_info"],"date":d["date"],"venue":d["venue"],"city":d["city"]}
        return json.dumps(x,indent=4),200


@app.route("/deleted",methods=["POST"])
def delete_event():
    #if request.method=="POST":
        headers={'Content-Type': 'application/json'}
        d=request.json
        manager.delete(d["event_id"])
        x={"Deleted":"Successful"}
        # x = {"event_id": d["event_id"], "name": d["name"], "event_info": d["event_info"], "date": d["date"],"venue": d["venue"], "city": d["city"]}
        return json.dumps(x,indent=4),200


@app.route("/update",methods=["POST"])
def update_event():
    #if request.method=="POST":
        headers={'Content-Type':'application/json'}
        d=request.json
        event = Event(d["event_id"], d["name"], d["event_info"], d["date"], d["venue"], d["city"])
        manager.update(event)
        # x={"Updated":"Successful"}
        x = {"event_id": d["event_id"], "name": d["name"], "event_info": d["event_info"], "date": d["date"],"venue": d["venue"], "city": d["city"]}
        return json.dumps(x,indent=4),200

@app.route("/read",methods=["POST"])
def read_event():
    #if request.method=="POST":
        headers={'Content-Type':'application/json'}
        d=request.json
        event = manager.read(d["event_id"])
        d={"event_id":event.get_event_id(),"name":event.get_name(),"event_info":event.get_info(),"date":event.get_date(),"venue":event.get_venue(),"city":event.get_city()}
        #print type(json.dumps(d,indent=4))
        #print type(jsonify(d))
        #return jsonify(d)
        return json.dumps(d,indent=4)


@app.route("/upcoming")
def upcoming_events():
    if request.method == "GET":
        event_list = manager.upcoming()
        d=[]
        for event in event_list:
            x={"event_id":event.get_event_id(),"name":event.get_name(),"event_info":event.get_info(),"date":event.get_date(),"venue":event.get_venue(),"city":event.get_city()}
            d.append(x)
        return json.dumps(d,indent=4),200


@app.route("/completed")
def completed_events():
    if request.method=="GET":
        event_list = manager.completed()
        d=[]
        for event in event_list:
            x={"event_id":event.get_event_id(),"name":event.get_name(),"event_info":event.get_info(),"date":event.get_date(),"venue":event.get_venue(),"city":event.get_city()}
            d.append(x)
        return json.dumps(d,indent=4),200


@app.route("/search-city",methods=["POST"])
def search_city():
    #if request.method=="GET":
        input=request.json
        city=input["city"]
        event_list = manager.search_city(city)
        d = []
        for event in event_list:
            print event.get_name()
            x = {"event_id": event.get_event_id(), "name": event.get_name(), "event_info": event.get_info(),
                 "date": event.get_date(), "venue": event.get_venue(), "city": event.get_city()}
            d.append(x)
        # print d
        return json.dumps(d, indent=4)


@app.route("/search-date",methods=["POST"])
def search_date():
    #if request.method=="GET":
        input = request.json
        date = input["date"]
        event_list = manager.search_date(date)
        d = []
        for event in event_list:
            x = {"event_id": event.get_event_id(), "name": event.get_name(), "event_info": event.get_info(),
                 "date": event.get_date(), "venue": event.get_venue(), "city": event.get_city()}
            d.append(x)
        return json.dumps(d, indent=4)


@app.route("/list",methods=["POST"])
def list_events():
    headers = {'Content-Type': 'application/json'}
    d = request.json
    # print d["date1"]
    # print d["date2"]
    event_list = manager.list_events(d["date1"],d["date2"])
    d = []
    for event in event_list:
        x = {"event_id": event.get_event_id(), "name": event.get_name(), "event_info": event.get_info(),
             "date": event.get_date(), "venue": event.get_venue(), "city": event.get_city()}
        d.append(x)
    # print json.dumps(d,indent=4)
    return json.dumps(d, indent=4)


if __name__=="__main__":
    app.run('0.0.0.0',8080,debug=True)