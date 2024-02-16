import numpy as np
first_list = []
with open('input.txt', 'r') as file:
    for line in file:
        first_list.append(line)
        print(first_list)

second_list = []
for i in first_list:
    ice_cream = sorted(i.replace(' ', ''))
    second_list.append(ice_cream)
    print(second_list)

third_list = []
for j in second_list:
    matcha = np.unique(j).tolist()
    third_list.append(matcha)
    print(third_list)

fourth_list = []
for even_num in third_list:
    for num in even_num:
        if int(num) % 2 == 0:
            fourth_list.append(int(num))

print(fourth_list)

fifth_list = []
for odd_num in third_list:
    for number in odd_num:
        if int(number) % 2 != 0:
            fifth_list.append(int(number))

print(fifth_list)

with open('output.txt', 'w') as file:
    file.write(str(first_list) + '\n\n')
    file.write(str(second_list) + '\n\n')
    file.write(str(third_list) + '\n\n')
    file.write(str(fourth_list) + '\n\n')
    file.write(str(fifth_list) + '\n\n')



