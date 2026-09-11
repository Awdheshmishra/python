nums = [[1, 2], [3, 4], [5, 6]]

# list comprehension
result = [num for sublist in nums for num in sublist]


# Har sublist ko nums se lo, phir us sublist ka har num lo, aur num ko result mein daal do.


# 2nd method 

# result = []
# for sublist in nums:
#     for num in sublist:
#         result.append(num)

print(result)