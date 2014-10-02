register:
	python setup.py register

.PHONY: register

upload:
	python setup.py sdist upload

.PHONY: upload
