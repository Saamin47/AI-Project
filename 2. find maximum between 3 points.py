num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if num1 > num2 and num3:
    print (f"{num1} is maximum")
elif num2 > num1 and num3:
    print(f"{num2} is maximum")
elif num3 > num2 and num1:
    print(f"{num3} is maximum")