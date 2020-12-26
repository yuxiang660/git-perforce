from p4_to_git import Config, Sync

import os
import logging
import unittest

logging.basicConfig(level=logging.DEBUG, format='sync_tests | %(message)s')

config_file = 'utests/mock/config.json'

class SyncTestSuite(unittest.TestCase):

    def setUp(self):
        print()

    def test_clone(self):
        Sync.do(Config(config_file))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
