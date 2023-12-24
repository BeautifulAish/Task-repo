# to get name
products = [{"name": "laptop", "price": 1000},
            {"name": "smartphone", "price": 500},
            {"name": "airpods", "price": 300},
            {"name": "watch", "price": 200},
            ]

print(type(products))
print(type(products[1]))


def is_affordable_name(Ishita):
    return len(Ishita["name"]) > 7


def is_affordable(item):
    return item["price"] < 500

    affordable_items_price = list(filter(is_affordable, products))
affordable_items_name = list(filter(is_affordable_name, products))

for i in affordable_items_price:
    print(i["price"],i["name"])

    i = 10
    name = "Ishita"
    print(i)
    print(name)
    print (name+str(i))
