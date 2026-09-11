s = "swiss"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)          #frequency counted

# count = 0
for ch in s:
    if freq[ch]==1:
        print("first non repeating char is: "+ch)
        break

        # count+=1
        # if count ==2:
        #     # break

        
        

     
