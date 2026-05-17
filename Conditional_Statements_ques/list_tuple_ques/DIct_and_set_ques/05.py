#Write a program to check whether two lists have at least one common element using sets. 
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
set1 = set(list1)
set2 = set(list2)
if set1.intersection(set2):
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common elements.")