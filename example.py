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
        args = (self, "Still in the same loop")
        loop2.queueInvocation(function, args)
        function2 = lambda loop, args : loop.quit()
        loop2.queueInvocation(function2, ())

function = lambda loop, args: args[0].printMessage(args[1])
args = (Example(), "Hello world")
loop = currentLoop()
loop.queueInvocation(function, args)
loop.run()
