import time
import threading


class Interval:
    """Periodically calls a callback function asynchronously"""

    def __init__(self, delay: float, callback: callable, *args, **kwargs):
        """
        Initializes the Interval object but does not start the timer

        Parameters:
            delay (float): the delay between callback in seconds
            callback (callable): to be invoked every time the timer times out
            *args, **kwargs: arguments to be passed to every callback call
        """

        self.delay = delay
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.running = False
        self.timer = None
        self.timer_start = None
        self.elapsed = 0

    def onCallback(self):
        """Invokes the callback if the Interval is in the running state"""

        self.callback(*self.args, **self.kwargs)
        if self.running:
            self.startTimer(self.delay)

    def startTimer(self, delay: float):
        """
        Starts the internal timer for the given delay

        Parameters:
            delay (float): the delay before the timer fires in seconds
        """

        self.timer_start = time.time()
        self.timer = threading.Timer(delay, self.onCallback)
        self.timer.start()

    def start(self):
        """Enter the running state and start the periodic timers"""

        needs_to_be_started = not self.running
        self.running = True

        if needs_to_be_started:
            self.startTimer(self.delay)

    def pause(self):
        """Pause the Interval"""

        self.elapsed = time.time() - self.timer_start
        self.cancel()

    def resume(self):
        """
        Resume the Interval with the amount of time left from the previous cycle prior to pausing
        Ie: if the delay is 10s and the Interval was paused 7s after the last callback call, the next callback 
        will be invoked 3s from the resume() call
        """

        needs_to_be_started = not self.running
        self.running = True

        if needs_to_be_started:
            self.startTimer(self.delay - self.elapsed)

    def cancel(self):
        """Stops the periodic callbacks and enteres the not running state"""

        self.running = False
        if self.timer != None:
            self.timer.cancel()
            self.timer = None
