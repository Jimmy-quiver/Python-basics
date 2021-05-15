#try except
number = int(input("Enter a number: "))
print(number)

#to prevent  your program from throwing an error such as that in the terminal when the user gives out a string intead of an actual nnumber as stated in your code, you can use the try except
try:
    value = int(input("Enter a value: "))
    print(value)
except ValueError:
    print("Invalid value")

try:
    answer = 10/0
except ZeroDivisionError as err:
    print(err)