n1 = int(input("Enter 1st number:\n"))
n2 = int(input("Enter 2nd number:\n"))
n3 = int(input("Enter 3rd number:\n"))

if n1 > n2 and n1 > n3:
    print(f"1st number that is {n1} is Greater")

elif n2 > n1 and n2 > n3:
    print(f"2nd number that is {n2} is Greater")

else:
    print(f"3rd number that is {n3} is Greater")
