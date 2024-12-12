import re
import math

with open("Day03/input.txt") as f:
    total = 0

    complete_instructions = ""
    while line := f.readline():
        complete_instructions += line.strip("\n")
    
    donts = [i.start() for i in re.finditer(r"don't\(\)", complete_instructions)]
    dos = [i.start() for i in re.finditer(r"do\(\)", complete_instructions)]

    print("donts", donts)
    print("dos", dos)
    
    ignore_sub = []
    k = 0
    for i in donts:
        for j in dos:
            if j > i:
                if k > 0 and ignore_sub[k-1][1] == j:
                    break
                else:
                    ignore_sub.append((i,j))
                    k += 1
                    break
    print(ignore_sub)

    #     instructions = re.findall(r'(mul\(\d{1,},\d{1,}\))', line)
        
    #     for i in instructions:
    #         nums = list(map(int, re.findall(r'\d{1,}', i)))
    #         total += math.prod(nums)

    # print(total)