import requests

req = requests.get('http://localhost:8000/password?length=12')

print(req.json())