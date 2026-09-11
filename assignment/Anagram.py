# Anagram ---> means both strings have same character in same frequency


s1= "listen"
s2= "silent" 
if len(s1) != len(s2):
    print( False)
    # print("not equal length")
else:
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch,0)+1
    for ch in s2:
        freq[ch] = freq.get(ch,0)-1
    isanagram = True
    for value in freq.values():
        if value != 0:
            isanagram = False
            break
    print(isanagram)
    # print("yes it is ")