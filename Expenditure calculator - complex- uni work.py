loop = int(input("Number of Expenses: "))
expenses_name = []
expenses_list = []
count = -1
for expen_name_list in range(loop):
    count+=1
    expenses_name.append(input("Name of Expenditure: "))
    expenses_list.append(input("Cost of " + str(expenses_name[count]) + ": " ))

print(sum([float(x) for x in expenses_list]))