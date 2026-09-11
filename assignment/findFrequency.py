nums = [1, 2, 2, 3, 1, 2, 4]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)