products = [{"name": "laptop", "price": 1000},
            {"name": "smartphone", "price": 500},
            {"name": "airpods", "price": 300},
            {"name": "watch", "price": 200},
            ]

print(type(products))
print(type(products[1]))

def is_affordable(item):
    return item["price"] < 500


affordable_items = list(filter(is_affordable, products))
#print(affordable_items[0]["name"] + str(affordable_items[0]["price"]))
#print(affordable_items[1]["name"] + str(affordable_items[1]["price"]))

# using loop we can access in same line
for i in affordable_items:
    print(i["price"])      #get only price
    
