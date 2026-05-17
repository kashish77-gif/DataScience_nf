#Write a program to sort a list of tuples based on tuple values.  
my_tuples = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
# Sort by the first element of the tuple
sorted_by_first = sorted(my_tuples, key=lambda x: x[0])
# Sort by the second element of the tuple
sorted_by_second = sorted(my_tuples, key=lambda x: x[1])
print("Sorted by first element:", sorted_by_first)
print("Sorted by second element:", sorted_by_second)