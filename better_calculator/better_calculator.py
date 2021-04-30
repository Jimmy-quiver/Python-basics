#BETTER CALCULATOR
num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)          
else:
    print("Invalid operator")    