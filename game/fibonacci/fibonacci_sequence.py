from game.fibonacci.fibonacci_sequence_generator import FibonacciSequenceGenerator
from game.fibonacci.abstract_fibonacci import AbstractFibonacci

class FibonacciSequence(AbstractFibonacci):
    def __init__(self, limit=None):
        self.limit = limit
        self.generator = FibonacciSequenceGenerator(self.limit)
        self.sequence = [] if self.limit == None else [*self.generator]

    def __contains__(self, number: int):
        if type(number) in [int, float]:
            number = int(number)
        else:
            raise TypeError
        
        while self.limit == None and (len(self.sequence) == 0 or number > self.sequence[-1]):
            self.sequence.append(next(self.generator))

        return number in self.sequence
