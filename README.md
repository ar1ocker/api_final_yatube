# YATUBE API

![picture alt](https://avatars.dzeninfra.ru/get-zen_doc/1107063/pub_5af739e4d7bf2190725110b0_5bf50a972a606000aaf365fd/scale_1200)

------------------

## Описание

YATUBE API - API предназначенный для управления постами, комментариями и подписками пользователя

------------------

## Установка

- Скачайте репозиторий

- Создайте и активируйте окружение

```bash
python3 -m venv venv
```

```bash
. venv/bin/activate
```

- Установите зависимости

```bash
pip3 install -r requirements.txt
```

- Выполните миграции

```
python3 manage.py migrate
```

- Запустите проект

```
python3 manage.py runserver
```

------------------

## Примеры запросов

В заголовке запросов для действий требующих авторизацию должно передаваться поле

```
Authorization: Bearer <token>
```

### **Получение токена**

```
POST <host>/api/v1/jwt/create
Content-Type: application/json

{
    "username": "<username>"
    "password": "<password>"
}
```

### **Получение/создание постов**

Методы: GET, POST, OPTIONS

Авторизация для получения: **не требуется**

```
<host>/api/v1/posts/
```

### **Работа с отдельным постом**

Методы: GET, POST, PUT, PATCH, DELETE, OPTIONS

Авторизация для получения: **не требуется**

```
<host>/api/v1/posts/<post_id>/
```

### **Получение/создание комментариев**

Методы: GET, POST, OPTIONS

Авторизация для получения: **не требуется**

```
<host>/api/v1/posts/<post_id>/comments/
```

### **Работа с отдельным комментарием**

Методы: GET, POST, PUT, PATCH, DELETE, OPTIONS

Авторизация для получения: **не требуется**

```
<host>/api/v1/posts/<post_id>/comments/<comment_id>/
```

### **Получение списка групп**

Методы: GET, POST, OPTIONS

Авторизация для получения: **не требуется**

```
<host>/api/v1/groups/
```

### **Получение подписок**

Методы: GET, POST, OPTIONS

Авторизация для получения: **необходима**

```
<host>/api/v1/follow/
```

------------------

Более подробная информация об api доступна по адресу **\<host\>/redoc/**
