import http.client
import json

conn = http.client.HTTPConnection("localhost", 8000)

headersList = {
 "Accept": "*/*",
 "User-Agent": "PTU_20 API browser" 
}

payload = ""

conn.request("GET", "/", payload, headersList)
response = conn.getresponse()
result = response.read()
data = json.loads(result)

# print(data[0]['title'])
# print(result.decode("utf-8"))

for post in data:
    for key, value in post.items():
        print(f"{key}: {value}")
