#!/usr/bin/python
from SimpleLoop import EventLoop

class Example:
    def printMessage(self, message):
        print message



function = lambda loop, args: args[0].printMessage(args[1])
args = (Example(), "Hello world")
loop = EventLoop()
loop.queueInvocation(function, args)
loop.run()
