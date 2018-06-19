*******************
# NetRequests Library
*******************

NetRequests is a HTTP library for SBHS students. It routes your
requests through the school proxy. Here's a basic usage example:

```python
from NetRequest import *

net = NetRequest(Proxy("proxyUsername", "proxyPassword")
response = net.get("https://www.google.com/") //Performs HTTP get on url
print(response)
```
