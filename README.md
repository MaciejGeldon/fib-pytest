# fib-pytest
## This is a simple example on how to use:
* pytest mark paramtrize
* custom mark for marking slow tests
* how to add custom marker to pytest.ini
* how to configure .coveragerc to not include empty files and omit test files for generating coverage report

## This repository is tagged by steps:
* step_1, writing fib function and two edge case tests
* step_2, adding some simple tests for fib sequence
* step_3, refactoring above tests using mark.parametrize
* step_4, adding slow tests and marking them
* step_5, adding config to count coverage only in fibonacci.py

## Installation
For linux users:    
**`make`**  
Will create new virtualenv and install pytest and pytest-cov.    
Otherwise use standard steps create new python virtual env and install requirements.txt

## Usage
* Run fast tests:   
``pytest -m "not slow"``  or ``make test``
* Run all tests:    
`` pytest ``
* Run fast test with coverage:    
``pytest -m "not slow" --cov=fibonacci`` or ``make coverage``

## Cleaning
* Clean .pyc files    
``make clean``
* Clean pytest cache folder    
``make clean_test_cache``