import requests

url = 'http://localhost:8000/restapi/api/v1/marvel_heroes/1678'
payload = {}
headers = {}
res = requests.get(url, data=payload, headers=headers)
print("GET command")
print(res.json)
print(res.text)

res = requests.delete(url, data=payload, headers=headers)
print("\DELETE command")
print(res.json)
print(res.text)

# Cannot for the life of me figure out why this breaks, the
# post command is working fine in both Postman and the Curl expression
# I am pretty sure there is a python syntax error or something
# however I am already spending way too much time on this simple test.
# headers = {"Content-Type": "application/json"}
# url = 'http://localhost:8000/restapi/api/v1/marvel_heroes/'
# payload = {
#     "fields": [{
#         "id": "1678",
#         "name": "Spider-Man (Peter Parker)",
#         "IDENTITY": "Secret Identity",
#         "ALIGN": "Good Characters", "EYE": "Hazel Eyes",
#         "HAIR": "Brown Hair", "SEX": "Male Characters",
#         "ALIVE": "Living Characters",
#         "FIRST APPEARANCE": "Aug-62",
#         "Year": "1962"
#     }]
# }
# res = requests.post(url, data=payload, headers=headers)
# print("POST command")
# print(res.json)
# print(res.text)

url = 'http://localhost:8000/restapi/api/v1/marvel_heroes/1678'
payload = {}
headers = {}
res = requests.get(url, data=payload, headers=headers)
print("GET command again")
print(res.json)
print(res.text)
