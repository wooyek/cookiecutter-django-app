BAKE_OPTIONS=--no-input

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

bake: ## generate project using defaults
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

watch: bake ## generate project using defaults and watch for changes
	watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.project_slug}}/

replay: BAKE_OPTIONS=--replay
replay: watch ## replay last cookiecutter run and watch for changes
	;

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

publish: ## package and upload a release
	git checkout develop
	git merge master --verbose
	git push origin develop --verbose
	git push origin master --verbose

sync: ## Sync master and develop branches in both directions
	git checkout develop
	git pull origin develop --verbose
	git checkout master
	git pull origin master --verbose
	git checkout develop
	git merge master --verbose
	git checkout master
	git merge develop --verbose
	git checkout develop

release: sync test test-all publish ## package and upload a release
	;

upgrade-requirements: ## compile and freeze requirements file
	pip-compile -U --allow-unsafe --annotate
