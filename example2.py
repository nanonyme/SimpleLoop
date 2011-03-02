#!/usr/bin/python
from SimpleLoop import *
event = createEvent(lambda x: "Eat my shorts", None)
recycleEvent(event)
event2 = createEvent(lambda x: "Eat my baggy pants too", None)
if event == event2:
    print "And this is how we recycle"
