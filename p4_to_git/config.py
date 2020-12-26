import json
import os
import logging

class Config:
    def __init__(self, config_file):
        assert os.path.exists(config_file)
        with open(config_file, 'r') as f:
            self._data = json.load(f)

    @property
    def repo_root(self):
        return self._data["repo_root"]

    @property
    def depot_paths(self):
        for path in  self._data["depot_paths"]:
            if path[-1] != r'/':
                logging.error(f'!!! Depot path {path} should end with "/" which represents a folder. "p4_to_git" does not support to clone a single file !!!')
                exit(1)
        return self._data["depot_paths"]

    @property
    def exclude_paths(self):
        return self._data["exclude_paths"]

    @property
    def timeout(self):
        return self._data["timeout"]
