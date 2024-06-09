# Task 1: Validating Calculations

value1 = 100 + 50 / 2 * 3 - 1
value2 = 100 + (50 / 2) * (3 - 1)
result = value1 == value2
print("Are", value1,"and", value2, "equal?",result)
if value1 > value2:
    print("value1 is greater than value2")  
if value1 < value2:
    print("value1 is less than value2")


#Task 2: Mix and Match

expression = 10 * 10 and 10 ** 2 == 100
print("the expression is: 10 * 10 and 10 ** 2 == 100")
print("I predict the outcome will be True") 
print("the expression is", expression)
