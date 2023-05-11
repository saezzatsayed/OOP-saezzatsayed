DOCS = docs

.ONESHELL:

.DEFAULT_GOAL := run

mypy:
	mypy classes.py
	mypy main.py --explicit-package-bases

uml_diagram:
	pyreverse -o png -p OLIPY .

create_folder:
	@mkdir -p $(DOCS)

create_docs: create_folder
	pdoc --force -o docs classes.py main.py
	pdoc --force --html -o docs classes.py main.py
	@echo "docs created."

test:
	python -m unittest test.py

coverage:
	coverage run test.py
	coverage html

req:
	touch requirements.txt
	echo requests > requirements.txt

venv/bin/activate: requirements.txt
	python3 -m venv venv
	pip install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate

run: venv
	python3 mixedFractions.py
