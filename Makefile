PY := /lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8

all: help

help:
	@echo ''
	@echo 'Usage:'
	@echo '	make clean'
	@echo '	- "clean the project"'

clean:
	@rm -rf output

clone_wxe_ap:
	@$(PY) p4_to_git.py clone config.wxe_ap.json

sync_wxe_ap:
	@$(PY) p4_to_git.py sync config.wxe_ap.json

sync_force_wxe_ap:
	@$(PY) p4_to_git.py sync config.wxe_ap.json -f

clone_wxe_ua:
	@$(PY) p4_to_git.py clone config.wxe_ua.json

sync_wxe_ua:
	@$(PY) p4_to_git.py sync config.wxe_ua.json

sync_force_wxe_ua:
	@$(PY) p4_to_git.py sync config.wxe_ua.json -f

.PHONY: help clean utests config clone_utests sync_utests

utests: command config clone_utests sync_utests

command:
	@$(PY) -m utests.command_tests -v

config:
	@$(PY) -m utests.config_tests -v

clone_utests: clean
	@$(PY) -m utests.clone_tests -v

sync_utests:
	@$(PY) -m utests.sync_tests -v
