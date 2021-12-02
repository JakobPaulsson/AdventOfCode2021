lines = open('input_p1.txt', 'r').readlines()
commands = []
for line in lines:
    commands.append(line.strip().split())
horizontal = 0
vertical = 0
for i in range(0, len(commands)):
    amount = int(commands[i][1])
    command = commands[i][0]
    if command == "forward":
        horizontal += amount
    if command == "down":
        vertical += amount
    if command == "up":
        vertical -= amount

print(horizontal*vertical)