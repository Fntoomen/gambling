import random
import matplotlib.pyplot as plt

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def calc(prizes, cost, money):
    spend = 0
    earned = 0

    while spend < money:
        spend += cost
        earned += random.choice(prizes)
    return spend, earned

prizes = [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
cost = 700
tries = 0

all_spend = [0]
all_earned = [0]
x_axis = [0]


for i in range(100000):
    money = random.randint(700, 1000000)
    spend, earned = calc(prizes, cost, money)
    all_spend.append(all_spend[-1]+spend)
    all_earned.append(all_earned[-1]+earned)
    tries += 1
    x_axis.append(tries)

averaged_spend = [mean(i) for i in zip(all_spend)]
averaged_earned = [mean(i) for i in zip(all_earned)]

plt.plot(x_axis, averaged_spend, label = "spend")
plt.plot(x_axis, averaged_earned, label = "earned")

plt.xlabel('tries')
plt.ylabel('averaged spend/earned')
plt.title('Gambiling')

plt.legend()
plt.show()
