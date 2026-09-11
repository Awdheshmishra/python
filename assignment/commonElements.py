list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set2 = set(list2)

result = []

for num in list1:
    if num in set2:
        result.append(num)

print(result)