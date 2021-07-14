from game.interval import Interval
from game.fibonacci import isFibonacci


class Game:
    """
    Holds the game state and performs all functions required to satisfy the following requirements:
    - Every X seconds it will display report, in frequency descending order, the list of numbers and their frequency.
    - User can 'halt' the timer to pause.
    - User can 'resume' the timer.
    - If the added number is one of the first 1000 numbers in the Fibonacci sequence, inputNumber() returns True
    """

    fibonacci_number_1000 = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

    def __init__(self, delay: float, output_frequency_callback: callable):
        """
        Initializes Game

        Parameters:
             delay (float): the time in seconds between output_frequency_callback calls
             output_frequency_callback (callable): to be called periodically with the updated frequency stats
                called with one positional argument in the form of [(number, frequency), ...] in descending frequency order
        """

        self.frequencies = {}
        self.output_frequency_callback = output_frequency_callback
        self.interval = Interval(delay, self.reportFrequencies)
        self.interval.start()

    def reportFrequencies(self):
        """
        Reports the current frequency data via the output_frequency_callback callback
        output_frequency_callback is called with one positional argument in the form of 
        [(number, frequency), ...] in descending frequency order
        """

        frequencies_list = list(self.frequencies.items())
        frequencies_list.sort(key=lambda i: i[1], reverse=True)

        self.output_frequency_callback(frequencies_list)

    def inputNumber(self, number: int):
        """
        add a number to the state of the Game, this contributes the the frequency reported via the output_frequency_callback
        and checks if the number added is one of the first 1000 Fibonacci sequence numbers

        Parameters:
            number (int): the number to be added and check if its in the Fibonacci sequence

        Returns:
            (bool) True of number is a positive Fibonacci number
        """

        number = int(number)
        if number < 0:
            raise ValueError

        self.frequencies[number] = self.frequencies.get(number, 0) + 1

        return number <= self.fibonacci_number_1000 and isFibonacci(number)

    def halt(self):
        """
        Pauses the periodic frequency reporting callback (output_frequency_callback)
        It will save the time already waited since the last output_frequency_callback call
        """

        self.interval.pause()

    def resume(self):
        """
        Resumes the periodic frequency reporting callback (output_frequency_callback)
        It will resume from how much time had already passed when between teh last output_frequency_callback call
        and the halt() call
        """

        self.interval.resume()
