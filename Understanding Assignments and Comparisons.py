# Task 1: Value Swapping

a = 10
b = 100

if a > b:
    print("a =",a,"b =",b," therefore a is greater than b")
else:
    print("a =",a,"b =",b," therefore b is greater than a")

placeholder = a
a = b 
b = placeholder

if a > b:
    print("a =",a,"b =",b," value a was switched with b, therefore  a is now greater than b")
else:
    print("a =",a,"b =",b," value a was not switched with value b, therefore b is still greater than a")