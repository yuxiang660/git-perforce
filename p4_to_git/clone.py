from .command import Command

import logging
import os

class Clone:
    @staticmethod
    def do(config):
        logging.debug(f'--- Start Clone at "{config.repo_root}" ---')

        if os.path.exists(config.repo_root):
            logging.error(f'!!! Cannot clone to existing folder, please remove folder "{config.repo_root}" before clone !!!')
            exit(1)
        os.makedirs(config.repo_root)

        # Step1: git init
        cmd_git_init = f"cd {config.repo_root} && git init"
        assert Command(cmd_git_init).communicate()
        # Step2: git p4 sync -v //depot@all
        sync_depot_paths = ' '.join([path + '@all' for path in config.depot_paths])
        cmd_git_sync = f"cd {config.repo_root} && git p4 sync {sync_depot_paths}"
        if logging.root.level <= logging.DEBUG:
            cmd_git_sync += " -v"
        assert Command(cmd_git_sync).communicate(config.timeout)
        # Step3: git branch master refs/remotes/p4/master
        cmd_create_master_branch = f"cd {config.repo_root} && git branch master refs/remotes/p4/master"
        assert Command(cmd_create_master_branch).communicate()
        # Step4: git branch dev refs/remotes/p4/master
        cmd_create_dev_branch = f"cd {config.repo_root} && git branch dev refs/remotes/p4/master"
        assert Command(cmd_create_dev_branch).communicate()
        # Step6: git checkout master
        cmd_checkout_files = f"cd {config.repo_root} && git checkout master"
        assert Command(cmd_checkout_files).communicate()

        logging.debug(f'--- Done Clone at "{config.repo_root}" ---')
