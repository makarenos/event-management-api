# Event Management API

REST API for managing events built with Django REST Framework.

## Stack

Python 3.11, Django 5.2, Django REST Framework, JWT, Docker

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Docker
```bash
docker-compose up --build
```

## API

Docs available at `http://localhost:8000/api/docs/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/users/register/ | Register user |
| POST | /api/token/ | Get JWT token |
| POST | /api/token/refresh/ | Refresh token |
| GET | /api/events/ | List events |
| POST | /api/events/ | Create event |
| GET | /api/events/{id}/ | Get event |
| PUT | /api/events/{id}/ | Update event |
| DELETE | /api/events/{id}/ | Delete event |
| POST | /api/events/{id}/register/ | Register for event |

## Auth

Pass token in header: `Authorization: Bearer <token>`