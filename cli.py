import sys
import time
from game import Game


def main():
    """
    Performs all functions required to satisfy the following requirements:
    1. On startup, the program will prompt the user for the number of seconds (X) between outputting the frequency of each number to the screen.
    2. Every X seconds the program will display, in frequency descending order, the list of numbers and their frequency.
    3. If the user enters 'halt' the timer should pause.
    4. If the user enters 'resume' the timer should resume.
    5. If the user enters a number that is one of the first 1000 numbers in the Fibonacci sequence, the system should alert "FIB"
    6. If the user enters 'quit', the application should output the numbers and their frequency, a farewell message, and finally terminate.
    """

    delay = float(input(
        'Please input the amount of time in seconds between emitting numbers and their frequency: '))
    game = Game(delay, printFrequencyUpdate)
    number_count = 0

    while True:
        user_input = input(
            f'\nPlease enter the {"first" if number_count == 0 else "next"} number: ')

        if user_input == 'quit':
            game.halt()
            print('')
            game.reportFrequencies()
            print('Thank you for playing, goodbye')
            break

        elif user_input == 'halt':
            game.halt()

        elif user_input == 'resume':
            game.resume()

        elif not user_input.isnumeric():
            print(f'"{user_input}" is not a valid positive integer')

        else:
            number_count += 1
            number = int(user_input)
            is_fibonacci = game.inputNumber(number)
            if is_fibonacci:
                print('FIB')


def printFrequencyUpdate(frequencies_list: list):
    """
    Prints above the user input line the numbers and frequencies

    Parameters:
        frequencies_list (list): list of numbers and their frequencies in the form of [(number, frequency), ...] 
                                 in descending frequency order
    """

    if len(frequencies_list) == 0:
        frequencies_string = '(no numbers listed yet)'
    else:
        frequencies_string = ', '.join(f'{k}:{v}' for [k, v] in frequencies_list)

    if '--inline' in sys.argv or '-i' in sys.argv:
        printAboveInput('(number:frequency)', frequencies_string,
                        'updated at', time.strftime('%H:%M:%S'))
    else:
        print('(number:frequency)', frequencies_string)


def printAboveInput(*args, sep=' '):
    """
    Clear the line above the current curser position and print the given values joined in a single line
    The given values to be printed and sep (separator) should not include (or resolve to strings that includes) new line 
    characters as this will then override the line the cursor is currently on (potentially including user input)

    Parameters:
        *args (any): values to be printed
        sep (string): separator placed between values (but not before the first or after the last value) 
    """

    sys.stdout.write(u"\u001b[s\u001b[A\u001b[K\u001b[1G")
    sys.stdout.write(sep.join(str(arg) for arg in args))
    sys.stdout.write(u"\u001b[u")
    sys.stdout.flush()


if __name__ == '__main__':
    main()
