DOCS = docs

.ONESHELL:

.DEFAULT_GOAL := run

create_doc_folder:
	@mkdir -p $(DOCS)

create_docs: create_doc_folder
	pdoc -o docs morse.py classes.py 
	pdoc --html -o docs morse.py classes.py 
	@echo "html docs created and saved in $(DOCS)"

mypy:
	mypy classes.py
	mypy morse.py --explicit-package-bases

uml_diagram:
	pyreverse -o png -p OLIPY .

req:
	touch requirements.txt
	echo requests > requirements.txt

venv/bin/activate: requirements.txt
	python3 -m venv venv
	pip install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate

run: venv
	python3 morse.py