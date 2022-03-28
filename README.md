### Описание:

Проект API для Yatube решает задачу по обмену данными между программами и сайтом Yatube.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd api_final_yatube 
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

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

```
http://127.0.0.1:8000/api/v1/posts/ - получение и создание публикаций.

{
"text": "string",
"image": "string",
"group": 0
}
```

```
http://127.0.0.1:8000/api/v1/posts/{id}/ - получение и изменение публикации.
```


```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ - получение и добавление комментариев.

{
"text": "string"
}
```

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ - получение и изменение комментария.

{
"text": "string"
}

```

```
http://127.0.0.1:8000/api/v1/groups/ - получение списка сообществ.
```

```
http://127.0.0.1:8000/api/v1/groups/{id}/ - информация о сообществе.
```

```
http://127.0.0.1:8000/api/v1/follow/ - просмотр подписчиков и создание подписки.

{
"following": "string"
}

```