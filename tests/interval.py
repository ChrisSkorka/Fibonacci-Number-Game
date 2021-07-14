import unittest
import unittest.mock as mock
from tests import ThreadTestCase
import time
from game.interval import Interval

class IntervalTestCase(ThreadTestCase):
    """Test game.interval.Interval"""
    
    def test_callback(self):
        """Test that the Interval invokes the callback at approriate times"""

        delay = 1
        callback = mock.Mock()
        interval = Interval(delay, callback)
        interval.start()

        self.assertThreadStarted()

        time.sleep(0.9) # wait until just before the 1s mark
        callback.assert_not_called()
        time.sleep(0.2) # wait until just after the 1s mark
        callback.assert_called_once_with()
        callback.reset_mock()

        time.sleep(0.8) # wait until just before the 2s mark
        callback.assert_not_called()
        time.sleep(0.2) # wait until just after the 2s mark
        callback.assert_called_once_with()

        interval.cancel()
        self.assertThreadStopped()

if __name__ == '__main__':
    unittest.main()