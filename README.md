# 🚀 Marketing Agency Backend API

Бэкенд-часть сервиса для маркетингового агентства, разработанная на **Django REST Framework** с использованием **PostgreSQL** и **Docker**.

Проект представляет собой RESTful API для управления заявками (лидами), услугами агентства и портфолио выполненных кейсов.

---

## 🛠 Технологический стек

* **Язык программирования:** Python 3.10+
* **Фреймворк:** Django, Django REST Framework (DRF)
* **База данных:** PostgreSQL
* **Контейнеризация:** Docker, Docker Compose
* **CORS:** django-cors-headers (для интеграции с фронтендом)

---

## ✨ Основной функционал и API Endpoints

### 📍 Эндпоинты API:
* **`POST /api/v1/leads/`** — Прием заявок от клиентов (имя, телефон, выбранный тариф, роль в компании, ссылка на сайт/Instagram, сообщение).
* **`GET /api/v1/services/`** — Получение списка оказываемых услуг агентства.
* **`GET /api/v1/portfolio/`** — Получение списка выполненных кейсов и работ.

### 🛡 Панель администратора:
* **`GET /admin/`** — Встроенная административная панель Django для удобного управления полученными заявками, услугами и портфолио.

---

## 📁 Структура проекта

```text
marketing-agency-site/
├── agency/                  # Основное Django-приложение (models, views, serializers, urls)
├── marketing_agency/        # Главные настройки проекта (settings.py, urls.py)
├── media/                   # Загружаемые медиафайлы (изображения кейсов/услуг)
├── docker-compose.yml       # Конфигурация Docker Compose (web + db)
├── Dockerfile               # Инструкция для сборки образа Django
├── manage.py                # Управляющий скрипт Django
└── requirements.txt         # Зависимости Python
