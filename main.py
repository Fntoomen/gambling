import random

def calc(wins, cost, money):
    spend = 0
    earned = 0
    won = 0
    tries = 0

    while spend < money:
        tries += 1
        spend += cost
        earned += random.choice(wins)
        if spend < earned:
            won += 1
    return {"won": won, "tries": tries}

won = 0
tries = 0
wins = [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
cost = 700
money = 10000

for i in range(10000):
    case = calc(wins, cost, money)
    won += case["won"]
    tries += case["tries"]

print(won/tries)
