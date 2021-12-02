lines = open('input_p2.txt', 'r').readlines()
commands = []
for line in lines:
    commands.append(line.strip().split())
horizontal = 0
vertical = 0
aim = 0
for i in range(0, len(commands)):
    amount = int(commands[i][1])
    command = commands[i][0]
    if command == "forward":
        horizontal += amount
        vertical += aim*amount
    if command == "down":
        aim += amount
    if command == "up":
        aim -= amount

print("horizontal: " + str(horizontal))
print("vertical: " + str(vertical))
print("aim: " + str(aim))
print(horizontal*vertical)