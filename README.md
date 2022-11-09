# Django-CRUD
CRUD refers to the four basic operations a software application should be able to perform – Create, Read, Update, and Delete.

# django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

## how django works

![](https://images.ctfassets.net/23aumh6u8s0i/59jLz45C9Sh420h7fJwEyP/c10bd09024e76223d12f69013fb3a3bf/django-flow)

## models
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.


## Documentation

[Documentation](https://www.djangoproject.com/)


## Run Locally

Clone the project

```bash
  git clone https://github.com/jamkia01010/Django-CRUD
```

Go to the project directory

```bash
  cd my-project
```

Install django

```bash
  pip install django
```

Start the server

```bash
  python ./mange.py runserver
```


## url Reference

#### Get all items

```http
  GET /blog/
```

| function |  Description                |
| :-------- | :------------------------- |
| `all_post` | here you well see all post in db |

#### Get item

```http
  GET /blog/<int:id>
```

| function |  Description                |
| :-------- | :------------------------- |
| `single_post` | here you well see single  post by id |

```http
  GET /blog/<int:id>/delete
```

| function |  Description                |
| :-------- | :------------------------- |
| `delete_post` | here delete post |


```http
  GET /blog/<int:id>/edit
```

| function |  Description                |
| :-------- | :------------------------- |
| `edit_post` | here you well edit post  |



