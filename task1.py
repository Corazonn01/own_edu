there_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 545, 234, 54345645576, 77]
making_list1 = []
for i in there_list:
    if i % 2 ==0:
        making_list1.append(str(i) + '-')
    else:
        making_list1.append(str(i))

final_one = [str(finall) for finall in making_list1]
print(' '.join(final_one))
