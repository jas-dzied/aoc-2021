with open('2.txt', 'r') as file:
    inputs = file.read().splitlines()
"""
x = 0
y = 0
for inp in inputs:
    parts = inp.split(' ')
    command = parts[0]
    amount = int(parts[1])
    if command == 'forward':
        x += amount
    elif command == 'down':
        y += amount
    elif command == 'up':
        y -= amount
print(x*y)
"""
x = 0
y = 0
aim = 0
for inp in inputs:
    parts = inp.split(' ')
    command = parts[0]
    amount = int(parts[1])
    if command == 'forward':
        x += amount
        y += (aim*amount)
    elif command == 'down':
        aim += amount
    elif command == 'up':
        aim -= amount
print(x*y)
