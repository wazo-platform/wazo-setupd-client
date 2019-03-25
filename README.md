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

### Get the current status of wazo-setupd

```python
client.status.get()
```

### Setup the Wazo engine

```python
body = {
    'engine_language': 'en_US',
    'engine_password': 'secret',
    'nestbox_host': 'nestbox.example.com',
    'nestbox_port': 443,
    'nestbox_service_id': 'nestbox-user',
    'nestbox_service_key': 'secret',
    'nestbox_instance_name': 'my-wazo',
    'nestbox_engine_host': 'wazo.example.com',
    'nestbox_engine_port': 443,
}
client.setup.create(body)
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
