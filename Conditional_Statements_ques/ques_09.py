#Write a program to determine whether a point lies in First quadrant, Second quadrant, Third quadrant, Fourth quadrant, On axis, or At origin. 
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
elif x == 0 and y == 0:
    print("At Origin")
else:
    print("On Axis")