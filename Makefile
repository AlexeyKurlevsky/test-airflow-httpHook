format:
	isort --lai 2 ./tasks ./dags
	black -l 120 ./tasks ./dags
lint:
	pylint ./tasks ./dags