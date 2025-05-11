#global variable & LOcal variable

x = 'awesome'

def myfunc():
  global x  # Declare that we are referring to the global variable x
  x = 'fantastic'  # Modify the global x

myfunc()  # Call the function to change the value of x
print('Python is ' + x)  # This will now print 'Python is fantastic'
 
#output will be Python is fantastic

#Example:
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

#output will be Python is awesome