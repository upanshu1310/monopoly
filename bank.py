from player import Player
import re
from datetime import date
import os

today = date.today()
d1 = today.strftime("%d-%m-%Y")

path = "C:/Users/Upanshu/Documents/Python/monopoly"

if not os.path.exists(f'{path}/{d1}'):
    os.mkdir(f'{path}/{d1}')
balances = open(f'{path}/{d1}/balances.txt', 'w')

ledger = []
players = {}

number = int(input("Enter number of players: "))
for i in range(number):
    name = input(f"Enter Player {i+1} Name: ")
    colour = input(f"Enter Player {i+1} colour (optional): ")
    players[name.lower()] = Player(name, colour)

commands = ["spend", "collect", "transfer", "history", "balance"]

while True:
    with open(f'{path}/{d1}/balances.txt', 'w') as f:
        for player in players.values():
            f.write(f'{player.name} - ${player.balance}\n')

    command = str(input("\nEnter command: "))

    if command == "exit":
        break

    elif command == "ledger":
        for entry in ledger:
            print(f'- {entry}')
        continue

    p1_name = re.match(r"^([^\.]+)", command).group(1).lower()
    if p1_name not in players:
        print("Invalid player")
        continue 
    p1 = players[p1_name]

    transactionType = re.search(r"\.([^.(]*)", command).group(1).lower()
    if transactionType not in commands:
        print("Invalid command")
        continue 

    amount = re.search(r"\d+", command)
    if amount is not None:
        amount = int(re.search(r"\d+", command).group())
        amt = "{:,}".format(amount)

    if transactionType == "spend":
        if p1.balance >= amount:
            note = f'{p1.name} spent ${amt}'
            ledger.append(note)
            p1.transactions.append(f"Spent ${amt}")
            p1.spend(amount)
        else:
            print(f'Insufficient funds!')
    
    elif transactionType == "collect":
        note = f'{p1.name} collected ${amt}'
        ledger.append(note)
        p1.transactions.append(f"Collected ${amt}")
        p1.collect(amount)

    elif transactionType == "transfer":
        if p1.balance >= amount:
            p2_name = re.search(r"\((\b[^,0-9]+)\b", command).group(1).lower()
            if p2_name not in players:
                print("Invalid player")
                continue
            p2 = players[p2_name]
            note = f'{p1.name} paid {p2.name} ${amt}'
            ledger.append(note)
            p1.transactions.append(f"Paid ${amt} to {p2.name}")
            p2.transactions.append(f"Received ${amt} from {p1.name}")
            p1.transfer(p2, amount)
        else:
            print(f'Insufficient funds!')

    elif transactionType == "history":
        for entry in p1.transactions:
            print(f'- {entry}')

    elif transactionType == "balance":
        bal = "{:,}".format(p1.balance)
        print(f'${bal}')
