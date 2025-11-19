import json 
import random

with open("cafeteria.json", "r") as file:
    data = json.load(file)

items = data["cafeteria"]["menu"]

print("Prices: ")

for item in items:
    price = 0
    randint = random.randint(1,3)
    if randint == 1: 
        price = item['price'] * 0.95
    elif randint == 2: 
        price = item['price'] * 0.9
    elif randint == 3: 
        price = item['price'] * 0.85

    print(f"{item['name']}: ${price}")
        
              