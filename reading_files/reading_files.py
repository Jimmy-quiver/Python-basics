#reading from external files in python
#open both the files inside th reading files folder


#there are a couple of different modes in which you can open external files
# 1. read denoted by "r" ->just reding
# 2. write denoted by "w" -> edit the file
# 3. append denoted by "a" -> add more info
# 4. read and write denoted by "r+"
employee_file = open("employee.txt","r")

print(employee_file.readable())

employee_file.close()