my_dict = {} #empty dictionary
print(my_dict)

my_dict = {1: 'Python', 2: 'Java'} #dictionary with elements
print(my_dict)

my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)

my_dict['Second'] = 'C++' #changing element
print(my_dict)

my_dict['Third'] = 'Ruby' #adding key-value pair
print(my_dict)

my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict.pop('Third') #pop element
print('Value:', a)
print('Dictionary:', my_dict)

b = my_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)

my_dict.clear() #empty dictionary
print('n', my_dict)

my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict['First']) #access elements using keys
print(my_dict.get('Second')) #access elements through value

my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
print(my_dict.keys()) #get keys
print(my_dict.values()) #get values
print(my_dict.items()) #get key-value pairs
print(my_dict.get('First'))