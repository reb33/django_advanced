# django_advanced

### команда для запуска миграций внутри контейнера

```aiignore
docker compose --env-file .env.prod -f docker-compose.prod.yml exec django_advanced python manage.py migrate --noinput
```

### сбор статики внутри контейнера

```aiignore
docker compose --env-file .env.prod -f docker-compose.prod.yml exec django_advanced python manage.py collectstatic --noinput
```