from yarl import URL

"""
Yarl is designed for easy and efficient URL management and analysis in Python. 
It handles encoding and decoding, allowing you to create, analyze and modify URLs in a simple way.
"""

url = URL('https://www.python.org/~guido?arg=1#frag')
# All url parts: scheme, user, password, host, port, path, query and fragment are accessible by properties:

scheme = url.scheme
print("The scheme is", scheme)

host = url.host
print("The host is ", host)

path = url.path
print("The url path is ", path)

query = url.query_string
print("The query string is ", query)

fragment = url.fragment
print("The fragment is ", fragment)

