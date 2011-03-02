#  Copyright 2011 Seppo Yli-Olli
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from collections import deque

_currentLoop = None

def currentLoop():
    global _currentLoop
    if not _currentLoop:
        _currentLoop = EventLoop()
    return _currentLoop


class EventLoop:

    def __init__ (self):
        self._queue = deque()
        self._running = False
        self._defaultInvocation = None
        self._currentLoop = self


    def queueInvocation(self, function, args):
        self._queue.append((function, args))

    def defaultInvocation(self, function, args):
        self._defaultInvocation = (function, args)

    def quit(self):
        self._running = False

    def run(self):
        self._running = True
        while True:
            if not self._running:
                break
            if len(self._queue) > 0:
                (function, args) = self._queue.popleft()
                function(self, args)
            elif self._defaultInvocation:
                (function, args) = self._defaultInvocation
                function(self, args)
            else:
                break


        
            
