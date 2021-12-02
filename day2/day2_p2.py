lines = open('input_p2.txt', 'r').readlines()
horizontal = 0
vertical = 0
aim = 0

for i in range(0, len(lines)):
    line = lines[i].strip().split()
    command = line[0]
    amount = int(line[1])
    if command == "forward":
        horizontal += amount
        vertical += aim*amount
    if command == "down":
        aim += amount
    if command == "up":
        aim -= amount

print(horizontal*vertical)