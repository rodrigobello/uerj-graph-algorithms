clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -name "*.pyc" -exec rm -f {} \;

test:
	python3 -m unittest discover ./src/tests

run:
	python3 main.py
