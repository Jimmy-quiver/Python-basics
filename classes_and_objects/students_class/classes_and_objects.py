# class just defines an item or person, in this case a student like a template
#an object is an actual item

from student import student

student1 = student("Jim", "Business", 3.1, False)
student2 = student("Jim", "Business", 3.1, False)

print(student1.name)