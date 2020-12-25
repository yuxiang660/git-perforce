import json
import os

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
        return self._data["depot_paths"]
