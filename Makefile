.PHONY: check publish test

check:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

init:
	pyenv virtualenv force_deps
	pyenv activate force_deps
	pip install --upgrade pip
	git init
	git add -A
	git commit -a -m "Initializing project"
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	python -c "import force_deps; print(force_deps.__version__) | xargs -i "git tag {} && git push origin {}"
	git push origin master

