from p4_to_git import Clone, Sync, Config
import argparse
import logging
import os

logging.basicConfig(level=logging.DEBUG, format='P4 TO GIT | %(message)s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='P4 TO GIT Tool')
    parser.add_argument('action', choices=['clone', 'sync'], help='choose action (clone or sync) for p4_to_git tool')
    parser.add_argument('config_file', help='configuration file for p4_to_git tool')
    parser.add_argument('-f', '--force', dest='sync_force', action='store_true', help='sync the reop forcely')
    args = parser.parse_args()

    config = Config(args.config_file)
    if args.action == 'clone':
        Clone.do(config)
    else:
        Sync.do(config, args.sync_force)


