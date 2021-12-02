lines = open('input_p1.txt', 'r').readlines()
numbers = []
for line in lines:
    numbers.append(int(line.strip()))

no_increased = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        no_increased += 1

print(no_increased)