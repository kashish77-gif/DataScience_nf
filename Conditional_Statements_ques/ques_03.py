# Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or special character. 
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")