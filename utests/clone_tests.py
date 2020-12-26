from p4_to_git import Config, Clone

import os
import logging
import unittest

logging.basicConfig(level=logging.INFO, format='clone_tests | %(message)s')

config_file = 'utests/mock/config.json'

class CloneTestSuite(unittest.TestCase):

    def setUp(self):
        print()

    def test_clone(self):
        Clone.do(Config(config_file))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
