run_server:
	python manage.py runserver
shell:
	python manage.py shell
create_superuser:
	python manage.py createsuperuser

run_migrate:
	python manage.py migrate
run_makemigrations:
	python manage.py makemigrations

pre_commit_run:
	pre-commit run --files

.PHONY: run_server,create_superuser
.PHONY: run_migrate,run_makemigrations
.PHONY: pre_commit_run
.PHONY: shell
