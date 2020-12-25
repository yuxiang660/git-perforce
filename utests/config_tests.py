from kit import Config

import os
import logging
import unittest

logging.basicConfig(level=logging.INFO, format='config_tests | %(message)s')

config_file = 'utests/mock/config.json'

class ConfigTestSuite(unittest.TestCase):

    def setUp(self):
        print()

    def test_get_config(self):
        c = Config(config_file)
        print(c.repo_root)
        print(c.depot_paths)

    def test_get_sync_depot_paths(self):
        c = Config(config_file)
        print(' '.join([path + '@all' for path in c.depot_paths]))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
