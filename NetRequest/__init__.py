"""
*******************
NetRequests Library
*******************

NetRequests is a HTTP library for students. It routes your http
requests through the school proxy.

:copyright: Copyright (c) 2017 Dawei Wu and Eric Holmstrom. All Rights Reserved.
:license: MIT, see LICENSE for more details.
"""

import urllib.request

class Header():
	def __init__(self, key, value):
		self.key = key
		self.value = value

class Proxy():
	def __init__(self, *args):
        num_args = len(args)
        
        if (num_args == 1):
            with open(args[0],"r") as f:
				self.username = self.normaliseUsername(f.readline())
				self.password = f.readline().strip()
                
		elif (num_args == 2):
			self.username = args[0]
			self.password = args[1]
            
		else:
			raise ValueError("Incorrect arguments supplied to Proxy constructor.")
            
        self._proxyUrl = "proxy.intranet:8080"
		self.setProxyUrl()
        
    def normaliseUsername(username):
        username = username.strip()
        
        if username.endswith('@detnsw'):
            username = username[:-7]
        
        

    def setProxyUrl(self):
        self.__url = "http://" + self.username + ":" + self.password + "@" + self._proxyUrl
        
	def proxyUrl(self, proxyUrl):
        self._proxyUrl = proxyUrl
		self.setProxyUrl()

	def get(self):
		return {
			"http": self.__url,
			"https": self.__url
		}

class NetRequest():
	def __init__(self, proxy = None):
		if proxy is not None:
            
            if isinstance(proxy, Proxy) or hasattr(proxy, 'get'):
                self.proxy = proxy
                urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler(proxy.get())))
            else:
                raise ValueError("Incorrect argument supplied to NetRequest constructor.")

	def get(self, url):
		return urllib.request.urlopen(url).read()

	def post(self, url, data = None, headers = None):
		if data is not None:
			data = urllib.parse.urlencode(data).encode()
		
        req = urllib.request.Request(url, data=data)
		
        if headers is not None:
			for header in headers:
				req.add_header(header.key, header.value)

		return urllib.request.urlopen(req).read()
