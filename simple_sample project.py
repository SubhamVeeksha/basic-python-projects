num1=input("Enter a value:")
num2=input("Enter b value:")
x=input()
a=int(num1)+int(num2)
b=int(num1)-int(num2)
c=int(num1)*int(num2)
d=int(num1)/int(num2)
if x=="+":
    print(f"Addition:{a}")
elif x=="-":
    print(f'Substraction:{b}')
elif x=="*":
    print(f'Multiplication:{c}')
elif x=="/":
    print(f'Division:{d}')
else:
    print(f'Error')