f_obj = open("one_hundred.txt", "r")

number = f_obj.read().split()
provided_list = []

for each_number in number:
    provided_list.append(int(each_number))

f_obj.close()

missing_list = []

for missing_number in range(101):
    if missing_number not in provided_list:
        missing_list.append(missing_number)

result_file = open("one_hundred_sorted.txt", "w")
result_file.write(str(missing_list))
result_file.close()

result_file = open("one_hundred_sorted.txt", "r")
print(result_file.read())
result_file.close()