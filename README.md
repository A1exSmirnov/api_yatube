### Описание:

Проект API для Yatube решает задачу по обмену данными между программами и сайтом Yatube. Пользователь через мобильное приложение или другую програму "клиент", сможет смотреть посты авторов на сайте Yatube, создавать и редактировать собственные посты, просматривать списки сообществ к которым можно добавлять посты и получать информацию о каждом посте отдельно.Так же можно добавлять к постам коментарии, редактировать их и смотреть чужие комментарии,подписываться на авторов постов и просматривать своих подписчиков.

### Как запустить проект:
##### инструкция для Windows
Скачайте установочные файлы и запустите их.
Python: www.python.org/downloads/
Git bash : https://gitforwindows.org/

##### инструкция для macOS
1.Запустите программу Терминал (или Terminal.app), она находится в директории /Applications/Utilities/.
2.Установите утилиты разработчика. Для этого в терминале запустите команду:
```
xcode-select --install
```
3.Во время установки система попросит подтвердить лицензию на установку. Соглашайтесь.
4.Устанавливаем менеджер пакетов brew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
5.Устанавливаем Python и Git:
```
brew install python@3.7 git
```
##### инструкция для Linux (Ubuntu)
1.Установите Python, для этого в терминале выполните команду:
```
sudo apt-get install python3.7
```
Перед установкой терминал попросит вас ввести пароль администратора — сделайте это.
2.Установите Git:
```
sudo apt-get install git 
```
##### Запустите Git Bash (если у вас Windows) или Терминал (на Linux/MacOS)
Перейдите в директорию,в которую будете клонировать репозиторий с проектом:
```
cd путь к директории/
```
Клонируйте репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd путь к директории/api_final_yatube 
```

Cоздать виртуальное окружение:
_Команда для установки виртуального окружения на Mac или Linux:_
```
python3 -m venv venv
```
_Команда для установки виртуального окружения на Windows:_
```
python -m venv venv
```

Запуск виртуального окружения:
_Команда на Mac или Linux:_
```
source venv/bin/activate
```
_Команда на Windows:_
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```



### Примеры запросов к API:

GET-запрос "http://127.0.0.1:8000/api/v1/posts/" - получение публикаций.
Пример ответа:
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2021-10-14T20:41:29.648Z",
"image": "string",
"group": 0
}
]
}
```
POST-запрос "http://127.0.0.1:8000/api/v1/posts/" - создание публикации.
Пример запроса:
```
{
"text": "string",
"image": "string",
"group": 0
}
```
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```


GET-запрос "http://127.0.0.1:8000/api/v1/posts/{id}/" - получение публикации.
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
PUT-запрос "http://127.0.0.1:8000/api/v1/posts/{id}/" - обновление публикации.
Пример запроса:
```
{
"text": "string",
"image": "string",
"group": 0
}
```
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
PUTCH-запрос "http://127.0.0.1:8000/api/v1/posts/{id}/" - частичное обновление публикации.
Пример запроса:
```
{
"text": "new string"
}
```
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "new string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
DELETE-запрос "http://127.0.0.1:8000/api/v1/posts/{id}/" - удаление публикации.

GET-запрос "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/" - получение комментариев.
Пример ответа:

```
[
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
]
```
POST-запрос "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/" -добавление комментария.
Пример запроса:
```
{
"text": "string"
}
```
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
GET-запрос "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/" - получение комментария.
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
POST-запрос "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/" - обновление комментария.
Пример запроса:
```
{
"text": "string"
}
```
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
PATCH-запрос "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/" - частичное обновление комментария.
Пример запроса:
```
{
"text": "new string"
}
```
Пример ответа:

```
{
"id": 0,
"author": "string",
"text": "new string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
DELETE-запрос "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/" - удаление комментария.

GET-запрос "http://127.0.0.1:8000/api/v1/groups/" - получение списка сообществ.
Пример ответа:
```
[
{
"id": 0,
"title": "string",
"slug": "string",
"description": "string"
}
]
```

GET-запрос "http://127.0.0.1:8000/api/v1/groups/{id}/" - информация о сообществе.
Пример ответа:
```
{
"id": 0,
"title": "string",
"slug": "string",
"description": "string"
}
```

GET-запрос "http://127.0.0.1:8000/api/v1/follow/" - просмотр подписчиков.
Пример ответа:
```
[
{
"user": "string",
"following": "string"
}
]

```
POST-запрос "http://127.0.0.1:8000/api/v1/follow/" - создание подписки.
Пример запроса:
```
{
"following": "string"
}
```
Пример ответа:
```
{
"user": "string",
"following": "string"
}

```
POST-запрос "http://127.0.0.1:8000/api/v1/jwt/create/" - получить JWT-токен.
Пример запроса:
```
{
"username": "string",
"password": "string"
}
```
Пример ответа:
```
{
"refresh": "string",
"access": "string"
}

```
POST-запрос "http://127.0.0.1:8000/api/v1/jwt/refresh/" - обновить JWT-токен.
Пример запроса:
```
{
"refresh": "string"
}
```
Пример ответа:
```
{
"access": "string"
}

```
POST-запрос "http://127.0.0.1:8000/api/v1/jwt/verify/" - проверить JWT-токен.
Пример запроса:
```
{
"token": "string"
}
```
Пример ответа:
```
{
"token": [
"Обязательное поле."
]
}

```
### Контакты:
[Email](mailto:cnccnc991@gmail.com)
