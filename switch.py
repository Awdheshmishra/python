""" us = 2
match us:
    case 1: print("monday")
    case 2: print("tuesday") """



a=int(input("enter the vale of a: "))
b=int(input("enter the value of b: "))
case=int(input("Press 1 for addition \n Press 2 for substraction \n Press 3 for multiplication \n press 4 for  division "))
match case:
     case 1: print("Addition of a and b is: ",a+b)
     case 2: print("substraction of a and b is: ",a-b)
     case 3: print("multiplication of a and b is: ", a*b)
     case 4: print("Division of a and b is: ", a/b)