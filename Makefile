format:
	isort --lai 2 ./tasks
	black -l 120 ./tasks
lint:
	pylint ./tasks