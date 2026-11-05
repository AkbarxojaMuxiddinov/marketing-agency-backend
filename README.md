<div align="center">
  <img src="assets/orbit-studio.svg" alt="ORBIT Studio API" width="100%">
  <br>
  <img src="https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-API-A30000?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/PostgreSQL-storage-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Compose">
  <p><strong>От первого касания до кейса в портфолио — один API.</strong></p>
</div>

ORBIT — API для сайта маркетингового агентства. Он объединяет каталог услуг, опубликованные работы, список клиентов, социальные ссылки и входящие лиды.

## Поток проекта

```mermaid
flowchart LR
    V[Посетитель сайта] --> S[Услуги]
    V --> P[Портфолио]
    V --> L[Форма заявки]
    L --> D[(Lead в PostgreSQL)]
    A[Команда агентства] --> ADM[Django Admin]
    ADM --> D
    ADM --> C[(Кейсы и клиенты)]
```

## API-карта

Все маршруты данных находятся под `/api/v1/`.

| Метод | Путь | Назначение |
|---|---|---|
| `GET`, `POST` | `/api/v1/services/` | Просмотр и создание услуг |
| `GET`, `POST` | `/api/v1/portfolio/` | Просмотр и создание проектов |
| `GET` | `/api/v1/clients/` | Активные клиенты в заданном порядке |
| `GET` | `/api/v1/social-links/` | Активные ссылки на Instagram и Telegram |
| `POST` | `/api/v1/leads/create/` | Отправить имя, телефон и сообщение |
| `GET` | `/` | Главная страница агентства |
| `GET` | `/admin/` | Администрирование контента и заявок |

## Контентная модель

```text
Service ───────────── каталог услуг и цена
Portfolio ─────────── кейс, изображение и ссылка
Client ────────────── логотип, сайт и порядок показа
SocialLink ────────── Instagram / Telegram
Lead ──────────────── контакт и статус обработки
```

## Запуск

```bash
pip install -r requirements.txt
docker compose up --build
```

После запуска примените миграции:

```bash
docker compose exec web python manage.py migrate
```

API работает на `http://localhost:8000`, административная панель — на `/admin/`. Docker Compose поднимает веб-сервис и PostgreSQL.

## Технологии

`Python` · `Django` · `Django REST Framework` · `PostgreSQL` · `Docker Compose` · `WhiteNoise`
