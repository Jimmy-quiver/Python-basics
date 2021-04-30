#IF STATEMENTS
#variable assigned a boolean
is_male = True
is_tall = True

#using 'and' operator
if is_male and is_tall:
    print("you are male and tall")
#using 'elif' and 'or' operator
elif is_male or is_tall:
    print("you are either male or tall") 
#using 'not' function       
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are tall but not male")   
#'else' do this if all the above conditions are false    
else:
    print("you are neither male nor tall")    