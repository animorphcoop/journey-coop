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

For running it in development (as described in vite.config.js)

```bash
npm run dev
```


4. Now run SSR app (continue Vite process in parallel)

```bash
python manage.py runserver
```
(first time start might be slow due to syncing Django with Vite and due to `journey_vite_prevent_unstyled_flash` template tag)

## Deployment
with uWSGI and Caddy on Debian (needs more complete description)


### Setup user

- ssh into the server
 
```bash
adduser las
```
```bash
usermod -aG sudo las
```
```bash
sudo apt install ufw
```
```bash
sudo ufw allow ssh
```
```bash
sudo ufw allow http
```
```bash
sudo ufw allow https
```
```bash
nano /etc/ssh/sshd_config
```
`PermitRootLogin yes` so it reads `PermitRootLogin no`


### Project setup on the server
- Setup keys & clone repo
- Deploy Key: https://docs.gitlab.com/ee/user/project/deploy_keys/ (create without password on user 'journey')
- Add to Github via Settings->Repository->Deploy keys (read only is fine)
- Follow installation steps (from the start + add local.py with sensitive creds)
- Apart from getting Django side ready, also bundle Vite assets as static
```bash
npm run build
```
(don't forget to run)
```bash
python manage.py collectstatic
```

### uwsgi
- Django guidelines with some modifications: https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/uwsgi/
- To run it need to first enable venv and allowed hosts

```bash
uwsgi --ini journey.ini
```

- When changing settings reload pid file to update changes in settings or ini
```
uwsgi --reload uwsgi/uwsgi_journey.pid
```

### Caddy
- https://caddyserver.com/docs/install#debian-ubuntu-raspbian
- (refer to Caddyfile)

```bash
caddy start
```