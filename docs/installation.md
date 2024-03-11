# Installation

## Step-by-step instructions

1. These steps also include the installation steps from the following packages:
    - [django-markdownx](https://neutronx.github.io/django-markdownx/)
    - [django-simple-history](https://django-simple-history.readthedocs.io/en/latest/)
    - [django-htmx](https://django-htmx.readthedocs.io/en/latest/)
    - [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) (required for modal functionality)

    Please see each packages documentation for detailed installation/usage instructions.

2. Install the 'django-easy-docs' package via pip:

    ```bash
    python -m pip install django-easy-docs
    ```

3. Add 'easy_docs', 'markdownx', 'django_htmx', and 'simple_history' to your INSTALLED_APPS in your settings.py file:

    ```python
    INSTALLED_APPS = [
        ...
        'easy_docs',
        'markdownx',
        'django_htmx',
        'simple_history',
        ...
    ]
    ```

4. Add the following to your urls.py file:

    ```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('markdownx/', include('markdownx.urls')), # We need this for the markdown editor/preview
        path('docs/', include('easy_docs.urls')),
        ...
    ]
    ```

5. Add the following to your middleware in your settings.py file:

    ```python
    MIDDLEWARE = [
        ...
        'simple_history.middleware.HistoryRequestMiddleware',
        'easy_docs.middleware.CurrentUserMiddleware',
        'django_htmx.middleware.HtmxMiddleware',
        ...
    ]
    ```

6. Run the command below to apply the migrations for the 'easy_docs' app:

    ```bash
    python manage.py migrate
    ```

7. Collect static files for proper rendering of the markdown editor/preview:

    ```bash
    python manage.py collectstatic
    ```

8. Add the following to your base template:
    {% raw %}
    ```html
    {% load easy_docs_tags %}
    <head>
        ...
        {% load_dependencies %}
        ...
    </head>
    ```
    {% endraw %}

9. Alternately, you can add the scripts for HTMX, Alpine JS, and easy docs CSS manually:
    {% raw %}
    ```html
    {% load static %}
    <head>
        ...
        <script src="https://unpkg.com/htmx.org/dist/htmx.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/2.8.0/alpine.js"></script>
        <link href="{% static 'easy_docs/css/styles.css' %}" rel="stylesheet">
        ...
    </head>
    ```
    {% endraw %}

10. Add [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to your base template:

{% raw %}
```html
{% load static %}
<head>
    ...
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    ...
</head>
<body>
    ...

<!-- Place at the bottom of the body -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
```
{% endraw %}
