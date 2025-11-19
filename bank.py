import json

with open("bank.json", "r") as file:
    data = json.load(file)

customers = data["bank"]["customers"]


for customer in customers:
    deposit = 0
    widthdrawl = 0 

    for transaction in customer["transactions"]:
        if transaction["type"] == "deposit":
            deposit += transaction["amount"]
        elif transaction["type"] == "withdrawal":
            widthdrawl += transaction["amount"]
    
    print(f"Name: {customer['name']}")
    print(f"Deposits: ${deposit}")
    print(f"Widthdrawls: ${widthdrawl}")
    print("="*50)

