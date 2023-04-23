.ONESHELL:

.DEFAULT_GOAL := run

mypy:
	mypy classes.py
	mypy statistics.py --explicit-package-bases

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
	python3 statistics.py
