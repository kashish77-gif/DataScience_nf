#Write a program to sort a dictionary by its values. 
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_dict)
