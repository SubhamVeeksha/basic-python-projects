#adding 2 numbers:
def add(a,b):
    return a+b
result1=add(3,5)
print(result1)


#adding 2 numbers:
def add_numbers(c,d):
    return c+d
result= add_numbers (9,5)
print(result)


#personal_info
def personal_info(name,age):
    print("Name:",name)
    print("Age:",age)
personal_info(age=30,name="Bhavana")


#output=Hello Bobby! Hi,Spoorty
def greet_user(name,greeting="Hello"):
    return greeting +","+name+"!"
greeting1= greet_user("Bobby")
greeting2= greet_user("Spoorthy","Hi")

print(greeting1)
print(greeting2)

#output: 10
global_var=10
def my_function():
    print(global_var)
print(global_var)