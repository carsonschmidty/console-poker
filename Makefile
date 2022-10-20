#
# Console Poker
#

PKG_NAME    := console-poker
PKG_VERSION := $(shell poetry version | awk '{print $$2}')

.PHONY: dev requirements update version help setup tui
.DEFAULT_GOAL := help

dev:  ## Run the application
	poetry run python main.py

tui:  ## Run the application with a TUI
	poetry run python tui/title.py

requirements:  ## Generate the requirements.txt file
	poetry export -f requirements.txt > requirements.txt

update:  ## Update project and tooling dependencies.
	poetry update

version:  ## Print the application version
	@echo "${PKG_VERSION}"

help:  ## Print Make usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

setup:
	poetry install
