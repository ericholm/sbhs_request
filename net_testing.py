from NetRequest import *

net = NetRequest(Proxy("proxyUsername", "proxyPassword"))
response = net.get("https://httpbin.org/ip")

print(response)
