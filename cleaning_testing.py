import json

with open('data/categorized_database.txt', 'r') as data1_doc:
    data1_json = json.load(data1_doc)

print(data1_json.keys())

with open('data/non_categorized_database.txt', 'r') as data2_doc:
    data2_json = json.load(data2_doc)

print(data2_json.keys())
