# -*- coding: utf-8 -*-
with open("D:\Серега\Универ\Python\clickky\ThirdTask\input.txt", "r", encoding="utf-8") as input:
    x = input.read()
    print(x)
    one = []
    long = []
    for i in x:
        if i == '1':
            one.append(i)
        elif len(one) == 0:
            continue
        else:
            long.append(len(one))
            one.clear()

with open("D:\Серега\Универ\Python\clickky\ThirdTask\output.txt", "w", encoding="utf-8") as output:
    output.write(str(max(long)))
