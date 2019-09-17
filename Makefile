.PHONY: check publish docs update_docs

check:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

docs:
	cd docs
	$(MAKE) clean
	$(MAKE) html
	cd ..

init:
	pyenv virtualenv force_deps && pyenv activate force_deps
	git init
	pip install --upgrade requirements.txt
	pip install --upgrade requirements-dev.txt

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	python -c "import force_deps; print(force_deps.__version__) | xargs -i "git tag {} && git push origin {}"
	git push origin master

update_docs:
	$(MAKE) docs
	git push origin master

test:black force_deps
	# Run black before tox to make sure formatting doesn't break python version
	black force_deps --target-version py37 -l 80
	tox --parallel auto
	flake8 force_deps

