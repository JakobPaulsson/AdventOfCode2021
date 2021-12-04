lines = open('input_p1.txt', 'r').readlines()
numbers = []
for line in lines:
    numbers.append(line.strip())

gamma = ""
epsilon = ""

for i in range(0, len(numbers[0])):
    zeros = 0
    ones = 0
    for j in range(0, len(numbers)):
        if numbers[j][i] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(epsilon,2)*int(gamma,2))
        

