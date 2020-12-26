from .command import Command
import logging
import os

class Sync:

    @staticmethod
    def do(config):
        logging.debug(f'--- Start Sync at "{config.repo_root}" ---')
        if not os.path.exists(os.path.join(config.repo_root, ".git")):
            logging.error(f'!!! Cannot sync at folder "{config.repo_root}" because it is not a git repository. Please clone it at first !!!')
            exit(1)

        # Step1: git p4 sync -v //depot@all
        sync_depot_paths = ' '.join([path + '@all' for path in config.depot_paths])
        cmd_git_sync = f"cd {config.repo_root} && git p4 sync -v {sync_depot_paths}"
        assert Command(cmd_git_sync).communicate(config.timeout)
        # Step2: git checkout dev
        cmd_checkout_dev = f"cd {config.repo_root} && git checkout dev"
        assert Command(cmd_checkout_dev).communicate()
        # Step3: git branch -f master refs/remotes/p4/master
        cmd_update_master = f"cd {config.repo_root} && git branch -f master refs/remotes/p4/master"
        assert Command(cmd_update_master).communicate()
        # Step6: git checkout master
        cmd_checkout_master = f"cd {config.repo_root} && git checkout master"
        assert Command(cmd_checkout_master).communicate()

        logging.debug(f'--- Done Sync at "{config.repo_root}" ---')