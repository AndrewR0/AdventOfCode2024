import re
import math

with open("Day03/input.txt") as f:
    total = 0
    while line := f.readline():

        instructions = re.findall(r'(mul\(\d{1,},\d{1,}\))', line)
        
        for i in instructions:
            nums = list(map(int, re.findall(r'\d{1,}', i)))
            total += math.prod(nums)

    print(total)