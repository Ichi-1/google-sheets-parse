## Команда для запуска проекта
```docker-compose up```
### После билда docker-compose доступны следующие ресурсы:
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
- Celery worker запускает две таски - одну на чтение таблицы и запись в базу, другую - проверка просроченной даты поставки и отправки данных в виде json в Телеграм канал https://t.me/notifyMyExpired
- Данные Google Sheets обрабатываются pandas
- За получение котировок ЦБР отвечают соответствующие функции из google-sheets/utils.py
- Для прямой записи в базу используется плагин create_engine из sqlachemy


### Фронтенд
Для получения и вывода данных на клиентской стороне в react-app я использую интервальные fetch запросы.
Альтернативный вариант - использование протокола websocket, но для данного proof-of-concept варианта я решил использовать http и получать данные через GET из API.


### Google Sheets

[Google Sheets](https://docs.google.com/spreadsheets/d/1ldvQcQqF8FGgQ1EFofaHRSJc7LdtbZyEWxr8O21_oMU/edit#gid=0)
