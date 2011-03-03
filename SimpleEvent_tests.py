import unittest
from SimpleEvent import *

# 
def run_test(function, args):
    try:
        function(args)
    except AssertionError:
        return False
    return True

class EventFactoryTests(unittest.TestCase):
    def setUp(self):
        self.factory = EventFactory()

    def tearDown(self):
        self.factory = None

    def test_negativeMaxCount(self):
        success = run_test(lambda (x, y): x.setMaxCount(y),
                           (self.factory, -5))
        self.assertEqual(success, False,
                         "Should have refused negative value")


    def test_recycleNone(self):
        success = run_test(lambda (x, y): x.recycleEvent(y),
                           (self.factory, None))
        self.assertEqual(success, False,
                         "Should have refused recycling None object")

    def test_recycleInt(self):
        success = run_test(lambda (x, y): x.recycleEvent(y),
                           (self.factory, 56))
        self.assertEqual(success, False,
                         "Should have refused recycling an integer")

if __name__ == '__main__':
        unittest.main()
