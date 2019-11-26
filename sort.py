list1 = {'1': 1, '2': 2}
list2 = list1
list1['1'] = 5
print(list1)
print(list2)
sum = list1['1'] + list2['1']
print(sum)
