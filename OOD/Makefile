DOCS = docs

.ONESHELL:

.DEFAULT_GOAL := run

mypy:
	mypy classes.py
	mypy PolygonArea.py --explicit-package-bases

uml_diagram:
	pyreverse -o pdf -p OLIPY .

create_folder:
	@mkdir -p $(DOCS)

create_docs: create_folder
	pdoc --force -o docs classes.py PolygonArea.py
	pdoc --force --html -o docs classes.py PolygonArea.py
	@echo "docs created."

req:
	touch requirements.txt
	echo requests > requirements.txt

venv/bin/activate: requirements.txt
	python3 -m venv venv
	pip install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate

run: venv
	python3 PolygonArea.py
