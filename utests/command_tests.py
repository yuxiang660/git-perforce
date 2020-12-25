from kit import Command

import os
import logging
import unittest

logging.basicConfig(level=logging.INFO, format='command_tests | %(message)s')

class CommandTestSuite(unittest.TestCase):
    log_file = 'output/utests/command_tests.log'

    @classmethod
    def setUpClass(cls):
        os.makedirs(os.path.dirname(cls.log_file), exist_ok=True)

    def setUp(self):
        print()

    def test_ls_cmd_log_file(self):
        cmd = Command('ls', self.log_file)
        runtime = cmd.communicate()
        self.assertEqual(True, runtime != 0)

    def test_ls_cmd_console(self):
        cmd = Command('ls')
        runtime = cmd.communicate()
        self.assertEqual(True, runtime != 0)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
