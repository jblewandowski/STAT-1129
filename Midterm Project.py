# QUESTION ONE
import matplotlib.pyplot as plt
import json

numbers = open("numbers.txt", "r")
num_lines = numbers.readlines()

counts = {}
for i in range(11):
    counts[str(i)] = 0

for line in num_lines:
    num_list = line.split(',')
    for i in range(11):
        counts[str(i)] += num_list.count(str(i))

for num, count in counts.items():
    print('There are', count, 'occurances of', num)

print(list(counts.values()))

plt.bar(counts.keys(), counts.values(), width=1)
plt.grid()
plt.title('Numbers.txt Histogram')
plt.show()

with open('numbers_counts.json', 'w') as output:
    json.dump(counts, output)

# import pandas as pd

# df = pd.read_csv('Netflix Data.csv')

# print(df)