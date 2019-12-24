import requests

r = requests.get(url = "http://127.0.0.1:8000/status")
print("status")
print(r.text)

r = requests.post("http://127.0.0.1:8000/tokenize", json = {"text" : "It Works baby!, yohoooo"})
print(r.json())

r = requests.post("http://127.0.0.1:8000/pos", json = {"text" : "It Works baby!, yohoooo"})
print(r.json())

r = requests.post("http://127.0.0.1:8000/ner", json = {"text" : "It Works baby!, yohoooo"})
print(r.json())
