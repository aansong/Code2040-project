
import requests 
import json

api_key = '1a4b5af2e17859894a38860bf2d69de2'
git_url = 'https://github.com/aansong/Code2040-project'
payload = {'token':api_key, 'github':git_url}
endpoint = "http://challenge.code2040.org/api/register"
r = requests.post(endpoint, data =payload)
print (r.text)