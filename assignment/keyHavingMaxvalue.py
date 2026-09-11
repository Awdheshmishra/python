data = {
    "A": 10,
    "B": 25,
    "C": 15,
    "D": 20
}

max_key = None
max_value = float('-inf')

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print(max_key)