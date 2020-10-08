import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 100, "name": "Bobby", "views": 100000}]

update = {"likes": 1200, "name": "Jerry", "views": 50}

response = requests.put(BASE + "video/" + str(1), data=data[0])
print(response.json())
response = requests.get(BASE + "video/1")
print(response.json())
response = requests.patch(BASE + "video/1", update)
print(response.json())
"""
response = requests.delete(BASE + "video/1")
print(response.json())
"""