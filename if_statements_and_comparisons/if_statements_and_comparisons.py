#IF STATEMENTS AND COMPARISONS
#equal sign (==)
#not equal sign (!=)
#greater than (>)
#less than (<)
#greater then or equal to (>=)
#less than or equal to (<=)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
#call out the function to execute the code
print(max_num(3, 40, 50))

#also this code below can work. notice the difference when using return statement
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)
#call out the function to execute the code
max_num(300, 40, 50)