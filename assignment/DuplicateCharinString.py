s = "programming"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

result = []

for ch in s:
    if freq[ch] > 1 and ch not in result:
        result.append(ch)

print(result)