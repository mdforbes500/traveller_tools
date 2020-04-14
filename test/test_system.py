#! /usr/bin/python

from context import traveller
import unittest

class TestSystemClass(unittest.TestCase):

    @classmethod
    def setUpSystem(traveller.System):
        pass
    

    

if __name__ == '__main__':
    unittest.main()