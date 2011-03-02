#!/usr/bin/python
from SimpleLoop import EventLoop, currentLoop

# Following avoids infinite loop that would normally
# be caused by calling itself from a message. Structure
# the program to avoid this, this is just for demonstration
# purposes.

class Example:
    def printMessage(self, message):
        print message
        loop2 = currentLoop()
        event = loop2.factory.createEvent(lambda x : x[0].printMessage(x[1]),
                                          (self, "Still in same loop"))
        loop2.queueInvocation(event)
        event = loop2.factory.createEvent(lambda x : x.quit())
        loop2.queueInvocation(event)


loop = EventLoop(True)
event = loop.factory.createEvent(lambda x :x[0].printMessage(x[1]), (Example(), "Hello world"))
loop.queueInvocation(event)
loop.run()
