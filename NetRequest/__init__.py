"""
*******************
NetRequests Library
*******************

NetRequests is a HTTP library for students. It auto-magically routes your
requests through the school proxy. Here's a basic usage example:

:copyright: (c) 2017 by Dawei Wu and Eric Holmstrom.
:license: Apache 2.0, see LICENSE for more details.
"""
import urllib.request

class Header():
	def __init__(self, key, value):
		self.key = key
		self.value = value

class Proxy():
	def __init__(self, *args):
		print(args)
		if (len(args) == 2):
			self.username = args[0]
			self.password = args[1]
		else:
			with open(args[0],"r") as f:
				self.username = f.readline().strip()
				self.password = f.readline().strip()
		self.__url = "http://" + self.username + ":" + self.password + "@proxy.intranet:8080"

	def setProxy(self, proxyUrl):
		self.__url = "http://" + self.username + ":" + self.password + "@" + proxyUrl

	def get(self):
		return {
			"http": self.__url,
			"https": self.__url
		}

class NetRequest():
	def __init__(self, proxy = None):
		self.proxy = proxy
		if proxy is not None:
			urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler(proxy.get())))

	def get(self, url):
		return urllib.request.urlopen(url).read()

	def post(self, url, data = None, headers = None):
		if data != None:
			data = urllib.parse.urlencode(data).encode()
		req = urllib.request.Request(url, data=data)
		if headers != None:
			for header in headers:
				req.add_header(header.key, header.value)

		return urllib.request.urlopen(req).read()
