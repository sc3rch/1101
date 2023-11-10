file = open("one_hundred.txt")

master_list = []

for line in file:
    if len(line) > 1:
        list_nums = line.split()
        # print(list_nums)
        list_nums = [int(i) for i in list_nums]
        # print(list_nums)
        master_list.extend(list_nums)

file.close()

missing_list = []

for r in range(100):
    if r not in master_list:
        print(f"{r} is not present")
        missing_list.append(r)
        
print(missing_list)