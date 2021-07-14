import unittest
import unittest.mock as mock
import traceback
import types
import time
import threading

class ThreadTestCase(unittest.TestCase):
    """Allows for safe testing of multithreaded functionality"""

    def setUp(self):
        """store the number of threads prior to the test"""

        self.historic_thread_counts = [threading.active_count()]

    def tearDown(self):
        """On tear down, check that all threads created since the start of the current tests have been stopped"""

        # time to destroy threads
        time.sleep(0.1)
        net_threads_created = threading.active_count() - self.historic_thread_counts[0]

        # attempt to cancel any threads created that were not terminated
        this_thread_id = threading.get_ident()
        for thread in threading.enumerate():
            # do not terminate the testing thread
            if this_thread_id != thread.ident:

                # cancel any timer threads
                if isinstance(thread, threading.Timer):
                    thread.cancel()

        self.assertEqual(net_threads_created, 0)
    
    def updateThreadCountHistory(self):
        """Update the lists of historic thread counts"""

        time.sleep(0.01) # allow time for thread count to be updated
        self.historic_thread_counts.append(threading.active_count())

    def assertThreadCount(self, count):
        """Assert that the current number of threads is equal to count"""

        self.updateThreadCountHistory()
        self.assertEqual(count, self.historic_thread_counts[-1])

    def assertThreadStarted(self, count=None):
        """
        Assert that threads have been started since the last thread count has been added to history.
        Note that threads that were started and stopped within that period are not included, only the net difference is
        considered.
        If count == None: assert any number of threads have been started
        Else: assert exactly count threads have been started
        """

        self.updateThreadCountHistory()
        difference_to_last_measurement = self.historic_thread_counts[-1] - self.historic_thread_counts[-2]
        
        if count == None:
            self.assertGreater(difference_to_last_measurement, 0)
        else:
            self.assertEqual(difference_to_last_measurement, count)

    def assertThreadStopped(self, count=None):
        """
        Assert that threads have been stopped since the last thread count has been added to history.
        Note that threads that were stopped and started within that period are not included, only the net difference is
        considered.
        If count == None: assert any number of threads have been stopped
        Else: assert exactly count threads have been stopped
        """

        self.updateThreadCountHistory()
        difference_to_last_measurement = self.historic_thread_counts[-2] - self.historic_thread_counts[-1]

        if count == None:
            self.assertGreater(difference_to_last_measurement, 0)
        else:
            self.assertEqual(difference_to_last_measurement, count)