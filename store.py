import json 

with open("store.json", "r") as file:
    data = json.load(file)

items = data["store"]["items"]

print("Old Prices:")
for item in items:
    print(item)
print("="*60)

print("New Prices:")
for item in items:
    if item["price"] > 50: 
        item["price"] *= 0.9 
    print(item)