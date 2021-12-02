import sys
with open('1.txt', 'r') as file:
    inputs = map(int, file.read().splitlines())

"""
counter = 0
last_input = sys.maxsize
for inp in inputs:
    if inp > last_input:
        counter += 1
    last_input = inp
print(counter)
"""

counter = 0
last_inputs = [sys.maxsize, sys.maxsize, sys.maxsize]
for inp in inputs:
    if last_inputs[1]+last_inputs[2]+inp > sum(last_inputs):
        counter += 1
    last_inputs.pop(0)
    last_inputs.append(inp)
print(counter)
