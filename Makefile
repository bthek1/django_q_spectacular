.PHONY: help pull-deploy push-deploy makemigrations migrate runserver createsuperuser collectstatic test install-nginx uninstall-nginx install-gunicorn uninstall-gunicorn

# Makefile

help:			## Show this help.
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

makemigrations: ## Make migrations
	python manage.py makemigrations

migrate: makemigrations ## Apply migrations
	python manage.py migrate

runserver: migrate ## Run the Django development server
	python manage.py runserver

superuser: ## Create a superuser
	python manage.py createsuperuser --no-input

collectstatic: ## Collect static files
	python manage.py collectstatic --noinput

test: ## Run tests
	pytest
	

install-redis: ## Install and start Redis
	@echo "Installing Redis..."
	@chmod +x ./scripts/install_redis.sh
	@./scripts/install_redis.sh
	@echo "Redis installation complete!"


uninstall-redis: ## Uninstall Redis
	@echo "Uninstalling Redis..."
	@chmod +x ./scripts/uninstall_redis.sh
	@./scripts/uninstall_redis.sh
	@echo "Redis uninstallation complete!"