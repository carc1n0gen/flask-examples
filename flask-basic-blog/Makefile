all: setup db dev-server


setup:
	test -e config.yml || cp config.example.yml config.yml
	test -d .venv || python -m venv .venv
	. .venv/bin/activate; pip install -r requirements.txt


setup-dev: setup
	. .venv/bin/activate; pip install -r requirements-dev.txt


db:
	. .venv/bin/activate; flask db upgrade


create-user:
	. .venv/bin/activate; flask create-user


dev-server:
	. .venv/bin/activate; flask --app app.create_app run --reload


clean:
	rm -rf .venv