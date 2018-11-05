# wazo-setupd-client

A python client library to access wazo-setupd

## Usage

### Creating a client

```python
from wazo_setupd_client import Client
client = Client('localhost', verify_certificate=False, token=<auth-token>)
```

## Config

### Getting the service configuration

```python
client.config.get()
```

## Debian package

Follow the following steps to build a debian package for wazo-setupd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-setupd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
