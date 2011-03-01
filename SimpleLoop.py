class EventLoop:

    def __init__ (self):
        self._queue = []
        self._defaultinvocation = None

    def queueInvocation(self, function, args):
        self._queue.append((function, args))

    def defaultInvocation(self, function, args):
        self._defaultinvocation = (function, args)

    def run(self):
        while True:
            if len(self._queue) > 0:
                (function, args) = self._queue.pop()
                function(self, args)
            elif self._defaultinvocation:
                (function, args) = self._defaultinvocation
                function(self, args)
            else:
                break
            
