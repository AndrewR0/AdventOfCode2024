with open("Day01/input.txt") as f:
    while line := f.readlines():
        line = [i.strip("\n") for i in line]

        smalls = []
        larges= []
        for l in line:
            x,y = l.split("   ")
            smalls.append(x)
            larges.append(y)
        
        total = 0
        for i in smalls:
            total += (int(i) * larges.count(i))
        print(total)