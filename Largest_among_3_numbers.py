n1=int(input("Enter 1st number:\n"))
n2=int(input("Enter 2nd number:\n"))
n3=int(input("Enter 3rd number:\n"))

if(n1>n2 and n1>n3):
    print("1st number is Greater")

elif(n2>n1 and n2>n3):
    print("2nd number is Greater")

else:
    print("3rd number is Greater")