PY := /lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8

all: help

help:
	@echo ''
	@echo 'Usage:'
	@echo '	make clean'
	@echo '	- "clean the project"'

clean:
	@rm -rf output

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
