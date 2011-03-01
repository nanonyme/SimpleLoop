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
            
