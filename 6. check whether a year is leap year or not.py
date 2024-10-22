year=int(input("enter any year:"))
if year % 4 == 0 and year % 100 != 0 :
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")