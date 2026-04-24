## must have
- python
- uv

## to run
```sh
cd path/to/quintessencia
uv sync
uv run python -m app.main
```

## docker
```sh
docker build -t quintessencia:v1.0 .
docker run -d --name quintessencia quintessencia:v1.0
```