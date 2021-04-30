#FUNCTIONS
#collection of code that performs the same task
#def (keyword for functions)
#name functions in all lower case
#those with two words remember to seperate them with an underscore '_'

def say_hi():
#anything that comes within the function must be indented    
    print("Hello User")

#call out the function to execute the code
say_hi()

#flow in execution of code that includes a function
print("top")
say_hi()
print("bottom")

#how to make your functions more efficient
#this is done by adding a parameter inside the function e.g, 'name'
def say_hi_withName(name):
    print("Hello " + name)

say_hi_withName("Mike")  
say_hi_withName("Hermit")  

#you can add as many parameters as possible to your function
def say_hi_withname_andAge(name, age):
    print("Hello " +name + " ,you are " + age + " years old")

say_hi_withname_andAge("Mike", "70")  
#you can also pass in the age 70 as an integer without the "".This is done by adding str() e.g,
   # print("Hello " +name + " ,you are " + str(age) + " years old") 