# NetRequests Library
NetRequests is a HTTP library for SBHS students. It routes your http requests through the school proxy, using user supplied credentials.

## Installation
Simply download the zip, or clone the repo. Import all from `NetRequest` within your python project.

## Usage
Simply create an instance of `Proxy` by passing in either your username and password, or the path to a file containing them on the first two lines.
```python
from NetRequest import *

credentials = Proxy('proxyUsername', 'proxyPassword')
credentialsFromFile = Proxy("~/.netrequest")
```

Use this proxy instance with the `NetRequest` class to perform requests.
```python
net = NetRequest(Proxy("proxyUsername", "proxyPassword"))

// Performs HTTP get on url
response = net.get("https://www.google.com/") 
print(response)

print('\r\n')

// Post some data
response = net.post("https://httpbin.org/post") 
print(response)
```

## Authors & License
Written by Eric Holmstrom and Dawei Wu.
See LICENSE for more details.