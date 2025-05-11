print((10>5) and ('apple'=='apple'))
#output:true

print((3<2)and ("banana"=="orange"))
#output=false

print((5>=3) and (10!=10))
#output=false

print(("car"=="car") or (7<9))
#output= true

print(("dog"=="cat")or(6<10))
#output=true

print((2==3)or (8>15))
#output=false

print(not(4<=3))
#output=true

print(not("orange"=="orange"))
#output=false

print(not((5>3)and("apple"!="banana")))
#output=false

print((10>5)and not(3<2))
#output=True

#11. Example: "or" and "not" operators combined
print(("cat" == "cat") or not (6 > 10))
#Output: True

#12. Example: Using parentheses for grouping expressions
print(((5 >= 3) and (10 != 10)) or (8 > 15))
#Output: False

#13. Example: Combining multiple "and" operators
print((2 < 5) and (10 == 10) and ("hello" != "world"))
#Output: True

#14. Example: Combining multiple "or" operators
print((7 < 3) or (5 >= 5) or ("apple" == "apple"))
#Output: True

#15. Example: Using "not" operator with an expression
print(not (10 > 5 and "car" != "car"))
#Output: True

#16. Example: Using "not" operator with "or" and "and"
print(not (5 > 3 or "dog" == "cat" and 7 < 5))
#Output: False

#17. Example: Combining "and" and "or" operators
print((5 > 3 and "apple" != "banana") or (8 == 8 or 6 < 10))
#Output: True

#18. Example: Combining "or" and "not" operators
print(("apple" == "banana" or not (6 > 10)))
#Output: True

#19. Example: Complex combination of "and", "or", and "not"
print(not (2 < 5 and (7 > 3 or "hello" == "world")))
#Output: False

#20. Example: Nested use of "and", "or", and "not" operators
print((not (5 > 3) and (10 != 10 or "car" == "car")))
#Output: False