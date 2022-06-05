import json

data = '{"firstName":"Furkan","lastName":"Çalışkan","age": 21}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstname" : "engin",
    "email" : "sad23@gmail.com"
}

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))