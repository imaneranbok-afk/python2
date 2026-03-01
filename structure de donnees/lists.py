my_list = [] #create empty list
print(my_list)

my_list = [1, 2, 3, 'example', 3.132] #creating list with data
print(my_list)

my_list = [1, 2, 3]
print(my_list)

my_list.append([555, 12]) #add as a single element
print(my_list)

my_list.extend([234, 'more_example']) #add as different elements
print(my_list)

my_list.insert(1, 'insert_example') #add element i
print(my_list)

my_list = [1, 2, 3, 'example', 3.132, 10, 30]

del my_list[5] #delete element at index 5
print(my_list)

my_list.remove('example') #remove element with value
print(my_list)

a = my_list.pop(1) #pop element from list
print('Popped Element: ', a, ' List remaining: ', my_list)

my_list.clear() #empty the list
print(my_list)

my_list = [1, 2, 3, 'example', 3.132, 10, 30]
for element in my_list: #access elements one by one
    print(element)

print(my_list) #access all elements
print(my_list[3]) #access index 3 element
print(my_list[0:2]) #access elements from 0 to 1 and exclude 2
print(my_list[::-1]) #access elements in reverse


my_list = [1, 2, 3, 10, 30, 10]
print(len(my_list)) #find length of list
print(my_list.index(10)) #find index of element that occurs first
print(my_list.count(10)) #find count of the element
print(sorted(my_list)) #print sorted list but not change original
my_list.sort(reverse=True) #sort original list
print(my_list)


list1 = [12, 14, 16, 18, 20]
# repetition operator *
l = list1 * 2
print(l)


# concatenation of two lists
# declaring the lists
list1 = [12, 14, 16, 18, 20]
list2 = [9, 10, 32, 54, 86]