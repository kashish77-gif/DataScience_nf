#Write a program to create a dictionary from two lists: one of keys and one of values. 
keys = ['name', 'age', 'city']
values = ['Kashish', 30, 'New York']
my_dict = dict(zip(keys, values))
print("Created dictionary:", my_dict)