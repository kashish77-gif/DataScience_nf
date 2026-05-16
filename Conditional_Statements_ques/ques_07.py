#Write a program to calculate income tax according to salary ranges. 
salary = float(input("Enter salary: "))

if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print("Income Tax =", tax)