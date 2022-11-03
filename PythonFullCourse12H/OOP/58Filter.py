#   filter() = creates a collection of elements from an iterable for which a function returns true
# 
#   filter(function, iterable)
# 

friends = [("Rachel", 19),
            ("Monica", 18),
            ("Phoebe", 17),
            ("Joey", 16),
            ("Chandler", 21),
            ("Ross", 20)]

Over_eighteen = lambda friend : friend[1] >= 18 
friends_over = filter(Over_eighteen, friends)
friends_over = list(filter(Over_eighteen, friends))

for i in friends_over:
    print(i)






