#RETURN STATEMENTS
#return will return a value back to the caller
def cube(num):
    print(num*num*num)

cube(3)
#now that is one way of executing the math with functions
#we can still use return to execute a math problem
def square(value):
    return value*value
#you cant't type any code after the return statement    

result = square(4)
print(result)
