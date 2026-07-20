import urllib.request
import urllib.error

req = urllib.request.Request(
    'http://127.0.0.1:8080/scenario/quick', 
    data=b'{"corridor":"hormuz"}', 
    headers={'Content-Type': 'application/json'}
)
try:
    response = urllib.request.urlopen(req)
    print(response.read().decode())
except urllib.error.HTTPError as e:
    print(e.read().decode())
