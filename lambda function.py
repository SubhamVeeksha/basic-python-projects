#adding of 2 numbers:
add=lambda x,y:x+y
result=add(330,320)
print(result)

#squaring of numbers:
square=lambda x:x**2
result1=square(300)
print(result1)

#finding the sum of 2 numbers(using lambda):
#num1=int(input('num1='))
#num2=int(input("num2="))
#add=lambda num1,num2:num1+num2
#sum=add(num1,num2)
#print(f"sum={sum}")

#finding the Area of Circle:
def area(radius):
    circleArea=3.14*(radius**2)
    return circleArea
radius=6
a=area(radius)
print(a)