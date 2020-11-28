# define the name of the virtual environment directory
VENV := .venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

clean:
	find . -type f -name '*.pyc' -delete

clean_test_cache:
	rm -rf .pytest_cache

test:
	pytest -m "not slow"

coverage:
	pytest -m "not slow" --cov=fibonacci


.PHONY: all venv clean clean_test_cache test