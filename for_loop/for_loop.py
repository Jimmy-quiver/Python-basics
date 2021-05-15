#for loops
#exm 1
for letter in "For loops":
    print(letter)


#exm 2 (using arrays)
friends = ["John", "Kim", "Kevin"]
for name in friends:
    print(name)
#exm 2.1
for index in range(len(friends)):
    print(friends[index])

#exm 3 (using numbers)
for index in range(10):
    print(index)
#exm 3.1
for index in range(3, 10):
    print(index)

#exm 4
for index in range(10):
    if index == 0:
        print("First iteration")
    elif index < 9:
        print("subsequent iterations")
    else:
        print("last iteration")

        