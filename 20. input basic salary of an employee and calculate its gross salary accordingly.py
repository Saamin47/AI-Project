basic_salary= int(input("enter basic salary:"))
if basic_salary <= 10000:
    hra= (20%100)*basic_salary
    da= (80%100)*basic_salary
    gross_salary=basic_salary+hra+da
    print(f"{gross_salary} gross salary")
elif basic_salary<=20000:
    hra2= (25%100)*basic_salary
    da2= (90%100)*basic_salary
    gross_salary2 = basic_salary+ hra2 + da2
    print(f"{gross_salary2} gross salary")
elif basic_salary>20000:
    hra3= (30%100)*basic_salary
    da3= (95%100)*basic_salary
    gross_salary3 = basic_salary + hra3 + da3
    print(f'{gross_salary3} gross salary')