import unittest
from tests.fibonacci import FibonacciTestCase
from tests.interval import IntervalTestCase
from tests.game import GameTestCase

def suite():
    """Test game, interval, and game"""
    
    suite = unittest.TestSuite()
    suite.addTest(FibonacciTestCase)
    suite.addTest(IntervalTestCase)
    suite.addTest(GameTestCase)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())