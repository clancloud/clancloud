# clancloud

## Goal
A tool to organize a family, team, ... clan

## Tech stack
**Flask**  
Django could be a better choice, but I like the freedom 
of Flask instead of learning Django and trying to fit my logic into it. 
Starlette is faster, but I don't like using async/await everywhere.
Python without a GIL will solve concrrency in a better way?

Generate HTML on the server and **HTMX** for interactivity.
Can I make something with components? 
Create python-html-components? Components need to get own data?

**Postgresql**
Do I need an ORM. Raw SQL? SqlAlchemy Core?
Does something like gajus/slonik exists for Python?

## Development

Create a venv or devcontainer of your own choice.
```
pip install -r requirements.txt
flask run --debug
```

## Production

### Docker

.env
```
POSTGRES_DB="clancloud"
POSTGRES_USER="clancloud"
POSTGRES_PASSWORD="your secret password"
```   

docker compose up

### Nginx

```
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Prefix /;
    }
     
     location /static/ {
        alias /......../clancloud/static/;
    }
}
```
