# fastapi-template

Quickly prototype backend services, deployment included.

## Development

The project consists in a Python package implemented with a [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).

Requirements:
- Python 3.9+
- Poetry

Install requirements:
```sh
$ poetry install
```

To run the app locally:
```sh
$ DEBUG=1 poetry run MyApi
```

To run the tests:
```sh
poetry run pytest
```

## Deployment

To build the Docker container:
```sh
docker build . -t myapi
```

To run the container:
```sh
$ docker run -p 8080:8080 myapi
```




