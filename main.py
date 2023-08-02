import random
import matplotlib.pyplot as plt

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def calc(wins, cost, money):
    spend = 0
    earned = 0

    while spend < money:
        spend += cost
        earned += random.choice(wins)
    return spend, earned

wins = [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
cost = 700
money = 10000
tries = 0

all_spend = []
all_earned = []
x_axis = []


for i in range(10000):
    tries += 1
    x_axis.append(tries)
    money = random.randint(700, 10000)
    spend, earned = calc(wins, cost, money)
    all_spend.append(spend)
    all_earned.append(earned)

averaged_spend = [mean(i) for i in zip(all_spend)]
averaged_earned = [mean(i) for i in zip(all_earned)]

plt.plot(x_axis, averaged_spend, label = "spend")
plt.plot(x_axis, averaged_earned, label = "earned")

plt.xlabel('tries')
plt.ylabel('averaged spend/earned')
plt.title('Gambiling')

plt.legend()
plt.show()
