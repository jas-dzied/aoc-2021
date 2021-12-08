with open('3.txt', 'r') as file:
    lines = file.read().splitlines()
"""
counts = [(column.count('0'), column.count('1')) for column in zip(*lines)]
gamma = int(''.join('0' if count[0]>count[1] else '1' for count in counts), 2)
epsilon = int(''.join('1' if count[0]>count[1] else '0' for count in counts), 2)
print(gamma*epsilon)
"""
import copy
remaining = copy.deepcopy(lines)
for i, line in enumerate(zip(*remaining)):
    sig = '0' if list(zip(*remaining))[i].count('0') > list(zip(*remaining))[i].count('1') else '1'
    remaining = list(filter(lambda x: x[i] == sig, remaining))
oxygen = int(remaining[0], 2)

remaining = copy.deepcopy(lines)
i = 0
while len(remaining) > 1:
    sig = '0' if list(zip(*remaining))[i].count('0') > list(zip(*remaining))[i].count('1') else '1'
    remaining = list(filter(lambda x: x[i] != sig, remaining))
    i += 1
co2 = int(remaining[0], 2)

print(oxygen*co2)
