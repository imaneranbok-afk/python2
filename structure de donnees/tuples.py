my_tuple = (1, 2, 3) #create tuple
print(my_tuple)

my_tuple2 = (1, 2, 3, 'edureka') #access elements

for x in my_tuple2:
    print(x)

print(my_tuple2)
print(my_tuple2[0])
print(my_tuple2[:])
print(my_tuple2[3][4])

my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5, 6) #add elements
print(my_tuple)

my_tuple = (1, 2, 3, ['french', 'python'], 3)
my_tuple[3][0] = 'english'

print(my_tuple)
print(my_tuple.count(3))
print(my_tuple.index(['english', 'python']))

tuple_tosort = (8, 4, 5)
sorted_tuple = sorted(tuple_tosort)
print(sorted_tuple) #returns a list


tuple_tosort = (3, 1, 4, 2)
sorted_tuple = tuple(sorted(tuple_tosort))
print(sorted_tuple)

names = ("Sara", "Ahmed", "Bouchra")
sorted_names = tuple(sorted(names))
print(sorted_names)


my_tuple = (1, 2, 3, ['python', 'english'], 3)
my_tuple[3].sort()
print(my_tuple)