with open("Day02/input.txt") as f:
    total = 0
    while line := f.readline():
        
        reports = [int(l.strip("\n")) for l in line.split(" ")]

        for i in range(len(reports)):
            new_lst = reports[:i] + reports[i+1:]
            flag = True
            is_proper_order = (new_lst == sorted(new_lst) or new_lst == sorted(new_lst, reverse=True))

            if not is_proper_order:
                continue

            for j in range(len(new_lst) - 1):
                diff = abs(new_lst[j] - new_lst[j+1])
                if (not 1 <= diff <= 3):
                    flag = False
                    break

            if flag:
                break
                
        if is_proper_order and flag:
            total += 1

        # reports = [int(l.strip("\n")) for l in line.split(" ")]
        
        # flag = False

        # proper_order = (reports == sorted(reports) or reports == sorted(reports, reverse=True))

        # if reports[0] > reports[1]: # decreasing
        #     for i in range(len(reports) - 2):
        #         if 1 <= reports[i] - reports[i+1] <= 3:
        #             flag = True
        #         else:
        #             if (i == len(reports) - 2) or (i <= len(reports) - 3 and 1 <= reports[i] - reports[i+2] <= 3):
        #                 flag = True
        #             else:
        #                 flag = False
        #                 break

        # elif reports[0] < reports[1]: # increasing
        #     for i in range(len(reports) - 1):
        #         if 1 <= reports[i+1] - reports[i] <= 3:
        #             flag = True
        #         else:
        #             if (i == len(reports) - 2) or (i <= len(reports) - 3 and 1 <= reports[i+2] - reports[i] <= 3):
        #                 flag = True
        #             else:
        #                 flag = False
        #                 break
                
        # else: # neither
        #     continue

        # if flag:
        #     total += 1
    print(total)