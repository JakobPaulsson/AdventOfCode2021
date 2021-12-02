lines = open('input_p2.txt', 'r').readlines()
arr = []
no_increased = 0
for line in lines:
    arr.append(int(line.strip()))
for i in range(0, len(arr)-3):
    if arr[i+1] + arr[i+2] + arr[i+3] > arr[i] + arr[i+1] + arr[i+2]: no_increased += 1
print(no_increased)