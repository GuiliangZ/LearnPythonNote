# sort() method = used with lists
# sort() function = used with iterables
# [] ==> list; () ==> tuple;
# sort(key = **, reverse) method is only for "list"
# xxx = sorted(tuple, key = ***) function can be used in other iterables, but return a list

from codecs import getreader


student = ["squidward", "Sandy","Patrick","Spongebob","Mr.Krabs"]
student_tuple = ("squidward", "Sandy","Patrick","Spongebob","Mr.Krabs")
student.sort(reverse=True)
sorted_student = sorted(student_tuple, reverse=True)
for i in student:
    print(i)
for i in sorted_student:
    print(i)

students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

students.sort()
for i in students:
    print(i)

#####!!!!! This line of code below, quiet not understand
grade = lambda grades:grades[1]
#students.sort(key = grade,reverse = True)
sorted_students = sorted(students, key = grade)
for i in sorted_students:
    print(i)

for i in students:
    print(i)

age = lambda ages:ages[2]
students.sort(key = age)
for i in students:
    print(i)



