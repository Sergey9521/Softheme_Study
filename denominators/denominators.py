x = abs(int(input('Input number: ')))
dels = []
for i in range(1, x+1):
    if x%i == 0:
        dels.append(i)

print(dels)