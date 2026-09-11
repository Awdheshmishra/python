nums = [1, 2, 2, 3, 1, 4, 3]

seen = set() 
result = []

for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)

# seen   check karega duplicate hai ya nahi
# result  final list banayega