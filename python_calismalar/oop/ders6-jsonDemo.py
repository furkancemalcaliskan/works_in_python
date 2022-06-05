

import json

with open("/Users/dejkoveci/Documents/Çalışmalarım/python çalışmalar/oop/users.json") as users:
    data = json.load(users)

    for x in range(5):
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["address"]["geo"]["lat"])

        