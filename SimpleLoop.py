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
from SimpleEvent import EventFactory
_currentLoop = None
_eventDisposal = []
def currentLoop():
    return _currentLoop


class EventLoop:

    def __init__ (self, factory=False):
        self._queue = deque()
        self._running = False
        self._defaultEvent = None
        self._currentLoop = self
        if factory:
            self.factory = EventFactory()
        else:
            self.factory = None
        global _currentLoop
        _currentLoop = self

    def queueEvent(self, event):
        event._loop = self
        self._queue.append(event)

    def defaultEvent(self, event):
        event._loop = self
        self._defaultEvent = event

    def quit(self):
        self._running = False

    def run(self):
        if self._running:
            return
        self._running = True
        while True:
            if not self._running:
                break
            if len(self._queue) > 0:
                event = self._queue.popleft()
                output = event.execute()
                if output:
                    print output
                if self.factory:
                    self.factory.recycleEvent(event)
            elif self._defaultEvent:
                event = self._defaultEvent
                output = event.execute()
                if output:
                    print output
            else:
                break


        
            
