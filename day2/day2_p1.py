lines = open('input_p1.txt', 'r').readlines()
horizontal = 0
vertical = 0

for i in range(0, len(lines)):
    line = lines[i].strip().split()
    command = line[0]
    amount = int(line[1])
    if command == "forward":
        horizontal += amount
    if command == "down":
        vertical += amount
    if command == "up":
        vertical -= amount

print(horizontal*vertical)