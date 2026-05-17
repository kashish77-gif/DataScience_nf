#Write a program to find the second largest element in a list.  
numbers = [12, 45, 7, 89, 23]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
    print("Second largest element:", second_largest)
else:
    print("There is no second largest element.")
    