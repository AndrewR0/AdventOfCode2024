
with open("Day01/input.txt") as f:
    while line := f.readlines():
        line = [i.strip("\n") for i in line]
        
        smalls = []
        larges= []
        for l in line:
            x,y = l.split("   ")
            smalls.append(x)
            larges.append(y)

        smalls.sort()
        larges.sort()
        # print(smalls, larges)
        total = 0
        while smalls:
            total += abs(int(smalls.pop()) - int(larges.pop()))
        print(total)
