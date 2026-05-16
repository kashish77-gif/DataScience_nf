# Write a program to assign grades based on marks and display distinction for high scores. 
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A+")
    print("Distinction")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")