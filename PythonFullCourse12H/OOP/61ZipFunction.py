# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each elements within the zip object
#

username = ["Dude", "Bro", "Mister"]
passwords = ("p@aaword", "abc123", "guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = dict(zip(username, passwords))
users_2 = zip(username,passwords,login_date)

print(type(users))

for key, value in users.items():
    print(key + " : "+ value)

for i in users_2:
    print(i)









