with open("Day02/input.txt") as f:
    total = 0
    while line := f.readline():
        
        reports = [int(l.strip("\n")) for l in line.split(" ")]

        flag = True

        if reports == sorted(reports) or reports == sorted(reports, reverse=True):
            for i in range(len(reports) - 1):
                if not 1 <= abs(reports[i] - reports[i+1]) <= 3:
                    flag = False

            if flag:
                total += 1
        continue
    print(total)