# Code Union Test Problem

### Разработан через **DjangoRestFramework, PostgreSQL, Docker** 
![DjangoRestFramework Version](https://img.shields.io/badge/djangorestframework-3.0.0-orange)
![PostgreSQL Version](https://img.shields.io/badge/postgre-3.0.0-blue.svg)

## Project architecture
```
├── code_union
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── email
├── main
│   ├── management.py
│       └── command
│             └── update_currency.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── auth_urls.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── services
│   ├── __init__.py
│   └── tasks.py
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── .gitignore
└── req.txt
```

## Запуск проекта
#### Clone the repository to your local machine:
>`git clone https://github.com/DauletKalesh/Code_Union.git`

#### To run the project:

>`docker-compose up --build`

#### For questions and support, feel free to contact me: dauka_0202@mail.ru