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

class EventFactory:
    def __init__(self):
        self._recycledObjects = []
        self._maxCount = 10

    def recycleEvent(self, event):
        if len(self._recycledObjects) < self._maxCount:
            event.__recycle__()
            self._recycledObjects.append(event)
        
    def createEvent(self, function, args=None):
        if len(self._recycledObjects):
            event = self._recycledObjects.pop()
            event.__init__(function, args)
            return event
        else:
            return Event(function, args)

    def setMaxCount(size):
        if size < 0:
            return
        self._maxCount = size
        while len(self._recycledObjects) < self._maxCount:
            self._recycledObjects.pop()                                                                


class Event:
    def __init__(self, function, args=None):
        self._function = function
        self._args = args
        self._loop = None

    def execute(self):
        if self._loop:
            if self._args:
                return self._function(self._args)
            else:
                return self._function(self._loop)

    def __recycle__(self):
        self._function = None
        self._args = None
        self._loop = None
