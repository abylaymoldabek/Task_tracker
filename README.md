## Это Таск менеджер проект.
## Здесь логика такая, что админ добавляет юзеров. Точнее наблюдателя и кто исполняет.
## Добавляется через админку - `{localhost}/admin/auth/user/add/`
## Login - `{localhost}/login/` добавляет через jwtToken
## Если хотите добавить - `{localhost}/api/task/` через пост метод
## GET, PUT, PATCH, DELETE эти методы можете использовать по - `{localhost}/api/task/id`
## Также есть Celery который отправляет в эмейл сообщение когда статус меняется, то есть есть определенное время когда меняются статус и юзер сам меняет


##Чтобы поднять проект - `docker-compose up`