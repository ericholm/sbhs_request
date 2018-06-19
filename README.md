*******************
# NetRequests Library
*******************

NetRequests is a HTTP library for SBHS students. It routes your
requests through the school proxy. Here's a basic usage example:

```python
from NetRequest import *

net = NetRequest()
response = net.get("")
print(response)
```
