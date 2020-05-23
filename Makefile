freeze:
	pipreqs . --force

format:
	black --config .\pyproject.toml .

install:
	pip install pipreqs
	pip install -r requirements.txt
