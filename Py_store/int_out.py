#!/usr/bin/python3

"""
file = open("JSON.txt", "w")
file.write("SON stands for JavaScript Object Notation. It is a lightweight format for storing and transporting data. JSON is often used when data is sent from a server to a web page. It is “self-describing” and easy to understand. JSON data is written as name/value pairs, just like JavaScript object properties. JSON objects are written inside curly braces, and JSON arrays are written inside square brackets. Here is an example of a JSON object! example:[]")
file.close()

file = open("Abednego_phibi_family.txt", "r")
my_info = file.read()
print(my_info)
file.close()


file = open("Abednego_phibi_family.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()

with open("Abednego_phibi_family.txt", "r") as file:
    content = file.read()
print(content)
"""
#how to convert json string to python

import json

data = {"name": "cleta", "age": 30, "city": "Nwe York"}
my_jsonsString = json.dumps(data)
print(my_jsonsString)

json_string = '{"name": "Exception", "age": 10, "city": "jos"}'
data = json.loads(json_string)
print(data)
