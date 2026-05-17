#Write a program to convert a tuple into a list and a list into a tuple. 
my_tuple = (1, 2, 3, 4, 5)
my_list = [6, 7, 8, 9, 10]
# Convert tuple to list
converted_list = list(my_tuple)
# Convert list to tuple
converted_tuple = tuple(my_list)
print("Converted list from tuple:", converted_list)
print("Converted tuple from list:", converted_tuple)
