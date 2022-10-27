import requests
import json
endpoint = "http://127.0.0.1:8000/machines/"

get_responce = requests.get(endpoint,json={"key":"value"})
print(get_responce.json())