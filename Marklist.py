m=int(input("Marks in maths:"))
s=int(input("Marks in science:"))
e=int(input("Marks in English:"))
total_marks=m+s+e
Average_marks=(total_marks/3)
percentage=(total_marks/300)*100

if percentage>90:
    grade="A"
elif percentage>80 and percentage<=90:
    grade="B"
elif percentage>70 and percentage<=80:
    grade="C"
elif percentage>60 and percentage<=70:
    grade="D"
elif percentage>50 and percentage<=60:
    grade="E"
else: 
    grade="FAIL"

print(f"Total marks:{total_marks}\nAverage marks:{Average_marks}\nGrade:{grade}")