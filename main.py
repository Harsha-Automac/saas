import requests
import json
endpoint = "http://127.0.0.1:8000/machines/info"

get_responce = requests.get(endpoint,json={"machine_id":"mid1"})
print(get_responce.json())