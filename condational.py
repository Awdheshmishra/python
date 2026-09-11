temp = int(input("enter temp: "))
humi = int (input("inter humidity: "))
if temp>=30 and temp<=40:
    if(humi>=40 and humi<=50):
    # if---humi>=40 and humi<=50

        print("it feels like 35")
    elif(humi>=50 and humi<=60):
    # elif--humi>=50 and humi<=60
        print("it feels like 45")  
else:
    print("invalid Entry")      