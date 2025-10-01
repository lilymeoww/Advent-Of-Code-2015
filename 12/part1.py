import json

def sum_all_integers(data):
    total = 0
    if isinstance(data, int):
        total += data
    elif isinstance(data, list):
        for item in data:
            total += sum_all_integers(item)
    elif isinstance(data, dict):
        for value in data.values():
            total += sum_all_integers(value)
    return total

with open("input.json") as jsonDataRaw:
    jsonData = json.loads(jsonDataRaw.readlines()[0].strip())

result = sum_all_integers(jsonData)
print(result)



