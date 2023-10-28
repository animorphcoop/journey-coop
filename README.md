# Journey to co-op

## What is it?

A community platform for sharing the life events that led people to join co-ops across the globe. People can share their
multimedia stories for other users to view and engage with.

The goal of the platform is to create an organic repository of inspiring stories and to facilitate a discussion on what
brings people into the co-op ecosystem.

## What is it made of?

Server-Side-Rendered web-app comprising of [Django](https://www.djangoproject.com/), [HTMX](https://htmx.org/), [Alpine.js](https://alpinejs.dev/) and [Tailwind CSS](https://tailwindcss.com/). The frontend (including Typescript
bundled with [Vite](https://github.com/MrBin99/django-vite/tree/master).

## What does it facilitate?

With a single-page-application feel, the website enables users to create accounts, post stories and respond to them
without refreshing.

## Setup & development

### PostgreSQL

1. Project uses PostreSQL database. Before being able to run the project properly, you need to install it on your
   device. On linux you need the following system packages:

```bash
sudo apt install postgresql postgresql-contrib libpq-dev python3-dev
```

2. Once installed, configure the db, user in line with `journey/dev.py`:

```bash
sudo -u postgres psql
```

```sql
CREATE
DATABASE journey_db_dev;
```

```sql
CREATE
USER journey_user_dev WITH ENCRYPTED PASSWORD 'local_testing_password';
```

```sql
ALTER
ROLE journey_user_dev SET client_encoding TO 'utf8';
ALTER
ROLE journey_user_dev SET default_transaction_isolation TO 'read committed';
ALTER
ROLE journey_user_dev SET timezone TO 'UTC';
```

```sql
GRANT
ALL
PRIVILEGES
ON
DATABASE
journey_db_dev TO journey_user_dev;
```

```sql
\q
```

### Django

1. Create virtual environment and activate it (after cloning and entering the project root dir):

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

2. Prepare Django for development

```bash
pip install -r dev_requirements.txt
```

```bash
python manage.py migrate
```

(after changes to the models)

```bash
python manage.py makemigrations
```

(if in doubt that some static assets have not been pulled)

```bash
python manage.py collectstatic
```

For making admin account

```bash
python manage.py createsuperuser
```

### Vite

Before running Django, open another terminal window to set up Vite to bundle frontend static assets

```bash
npm install
```

For running it in development (as described in vite.config.js)

4. Now run SSR app (continue Vite process in parallel)

```bash
python manage.py runserver
```

## Deployment

with uWSGI and Caddy on Debian

### Project setup on the server

1. Setup keys & clone repo
2. Follow installation steps above (from the start, install requirements.txt, add local.py with secrets, make sure there
   is a match with PostgreSQL credentials)

3. Build static assets
```bash
npm run build


3.Export production settings

```bash
export DJANGO_SETTINGS_MODULE='journey.prod'
```

4. Collect static files

```bash
python manage.py collectstatic
```

### uwsgi

journey.ini is creating a pid and log in uwsgi directory

To start uwsgi:

```bash
uwsgi --ini journey.ini
```

- When changing settings reload pid file to update changes in settings or ini

```
uwsgi --reload uwsgi/uwsgi_journey.pid
```

### Caddy

- Please refer to Caddyfile, it has been moved to /etc/caddy/)

```bash
caddy start
```

- if you change the config don't forget to reload

```bash
caddy reload --config /etc/caddy/Caddyfile
```

## Running Tests

In order to run tests before to push your changes to main branch or create a Pull Request, you need to install a couple
of libraries:

```bash
pip install -r dev_requirements.txt
```

Then you have to measure your code coverage, ideally always maintain at least a 90% of cc.

```bash
coverage run --source='.' manage.py test
coverage report
```

If you would like to analyze visually the lines of code covered by the tests, you should run this command after the
previous commands:

```bash
coverage html
```

This will generate an html report inside the folder htmlcov/.
For further info, please visit [coverage docs](https://coverage.readthedocs.io/en/7.3.2/)
