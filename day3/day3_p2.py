lines = open('input_p2.txt', 'r').readlines()
numbers = []
numbers2 = []
for line in lines:
    numbers.append(line.strip())
    numbers2.append(line.strip())

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
    most_of_num = ""
    if zeros > ones:
        most_of_num = "0"
    else:
        most_of_num = "1"
    j = 0
    while j < len(numbers):
        if len(numbers) == 1:
            break
        if numbers[j][i] == most_of_num:
            j += 1
        else:
            numbers.pop(j)

for i in range(0, len(numbers2[0])):
    zeros = 0
    ones = 0
    for j in range(0, len(numbers2)):
        if numbers2[j][i] == "0":
            zeros += 1
        else:
            ones += 1
    most_of_num = ""
    if zeros > ones:
        most_of_num = "0"
    else:
        most_of_num = "1"
    j = 0
    while j < len(numbers2):
        if len(numbers2) == 1:
            break
        if numbers2[j][i] == most_of_num:
            numbers2.pop(j)
        else:
            j += 1

print(int(numbers[0],2)*int(numbers2[0],2))