from abc import ABC, abstractmethod

class AbstractFibonacci(ABC):

    @abstractmethod
    def __contains__(self, value):
        pass