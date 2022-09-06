## Команда для запуска проекта
```docker-compose up -d --no-cache```
### После запуска доступны следующие ресурсы:
- Django (API Schema) http://localhost:8000
- React app http://localhost:3000

## Tech stack
- Django + DRF
- Docker + docker-compose
- PostgreSQL
- Celery + Redis
- React

  
### Описание
Приложение направленно на автоматизацию сбора данных из Google Sheets, парсинга и добавления в PostgeSQL.
Автоматизация организована с помощью таск-менеджера Celery + Redis (backend/apps/google-sheets/tasks.py).
- Celery worker запускает таску каждые 10 секунд
- Данные Google Sheets обрабатываются pandas
- За получение котировок ЦБР отвечают соответствующие функции из google-sheets/utils.py
- Для прямой записи в базу используется плагин create_engine из sqlachemy


### Фронтенд
Для получения и вывода данных на клиентской стороне в react-app я использую интервальные fetch запросы.
Альтернативный вариант - использование протокола websocket, но для данного proof-of-concept варианта я решил использовать http и получать данные через GET из API.

