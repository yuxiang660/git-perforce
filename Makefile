PY := /lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8

all: help

help:
	@echo ''
	@echo 'Usage:'
	@echo '	make clean'
	@echo '	- "clean the project"'

clean:
	@rm -rf output

.PHONY: help clean utests command

utests: command

command:
	@$(PY) -m utests.command_tests -v