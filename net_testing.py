from NetRequest import *

p = Proxy('user@!., |`3+= @detnsw', 'pass')
print(p.username)
print(p.get()['http'])

net = NetRequest(Proxy("proxyUsername", "proxyPassword"))
response = net.get("https://httpbin.org/ip")

print(response)
