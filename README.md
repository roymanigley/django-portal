# Portal
> Django app for a portal using mosaik grid style

## Usage

### developpment

#### initial
```
./python -m venv .venv
./manage.py createsuperuser
./manage.py compile messages
./manage.py migrate
```
#### running the service
```
./manage.py runserver
```

### docker
```
.
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
└── nginx
    ├── generate-keys.sh
    ├── keys (will be created by 'generate-keys.sh')
    └── nginx.conf
```
#### initial
```
cd nginx
./generate-keys.sh
```

#### running the service
```
docker compose up -d
```
