test:
	python3 -m pylint ker
doc:
	pdoc --html --output-dir docs ker --force
compile:
	python3 setup.py sdist bdist_wheel
publish:
	make compile && python3 -m twine upload --skip-existing dist/*
.PHONY: test
