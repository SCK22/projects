from django.test import TestCase

# Create your tests here.
import requests
import numpy as np

r = requests.get(url = "http://localhost:8000/status")
print("status")
print(r.text)


for _ in range(100):
    r = requests.post("http://localhost:8000/receiveEvents", json = {"data" : {"col1" : np.random.normal(25,5), "col2" : np.random.normal(20,5)}, "dataset" : "temp"})
print(r.json())


