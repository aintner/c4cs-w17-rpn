test:
	coverage run test_rpn.py
	python3 -m unittest
.PHONY: test
