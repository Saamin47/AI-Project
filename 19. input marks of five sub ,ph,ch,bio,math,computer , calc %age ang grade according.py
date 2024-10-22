physics = int(input("enter marks of physics:"))
chemistry = int(input("enter marks of chemistry:"))
biology = int(input("enter marks of biology:"))
math = int(input("enter marks of math:"))
computer = int(input("enter marks of computer:"))
marks_out_of = int(input("enter marks out of:"))
total = (physics+ chemistry + biology + math + computer)
percentage= marks_out_of / total * 100
if percentage >= 90 :
    print(f"{percentage} % with grade A")
elif percentage >=80 :
    print(f"{percentage} % with grade B")
elif percentage >=70 :
    print(f"{percentage} % with grade C")
elif percentage >=60 :
    print(f"{percentage} % with grade D")
elif percentage >=40 :
    print(f"{percentage} % with grade E")
elif percentage <40 :
    print(f"{percentage} % with grade F")