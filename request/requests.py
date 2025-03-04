import requests

class Url:

    password = requests.get('http://localhost:8000/password?length=12')

