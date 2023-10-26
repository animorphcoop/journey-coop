# Journey to co-op

## What is it?
A community platform for sharing the life events that led people to join co-ops across the globe. People can share their multimedia stories for other users to view and engage with.

The goal of the platform is to create an organic repository of inspiring stories and to facilitate a discussion on what brings people into the co-op ecosystem.

## What is it made of?
Server-Side-Rendered web-app comprising of Django, HTMX, Alpine.js and Tailwind. The frontend (including Typescript bundled with Vite. 

## What does it facilitate?
With a single-page-application feel, the website enables users to create accounts, post stories and respond to them without refreshing.


## Setup & development 

1. Create virtual environment and activate it (after cloning and entering the project root dir):

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

2. Prepare for running Django base

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

(after changes to the models)
```bash
python manage.py makemigrations
```
(if in doubt that some static assets have not been pulled
```bash
python manage.py collectstatic
```

For making admin account
```bash
python manage.py createsuperuser
```


3. Before running Django, open another terminal window to set up Vite to bundle frontend

```bash
npm install
```

~~For running it in development (as described in vite.config.js)~~

Give [the issue with reload loop](https://github.com/animorphcoop/journey-coop/issues/7), for now replace the standard development command `npm run dev` with entr:

```bash
find main/templates | entr -s 'npm run build'
```


4. Now run SSR app (continue Vite/entr process in parallel if needed but if it's building might not need to run)

```bash
python manage.py runserver
```

## Deployment
with uWSGI and Caddy on Debian 

### Project setup on the server
- Setup keys & clone repo
- Follow installation steps above (from the start + add local.py with sensitive creds)
```bash
npm run build
```
(don't forget to run)
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
In order to run tests before to push your changes to main branch or create a Pull Request, you need to install a couple of libraries:

```bash
pip install -r dev_requirements.txt
```

Then you have to measure your code coverage, ideally always maintain at least a 90% of cc.

```bash
coverage run --source='.' manage.py test
coverage report
```

If you would like to analyze visually the lines of code covered by the tests, you should run this command after the previous commands:

```bash
coverage html
```

This will generate an html report inside the folder htmlcov/.
For further info, please visit [coverage docs](https://coverage.readthedocs.io/en/7.3.2/)
