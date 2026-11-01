# This is a if-elif-else statement program
age = int(input("Enter your age: "))

if age <= 0:
    print("Invalid age!")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 35:
    print("Young Adult")
elif age <= 60:
    print("Middle-Aged Adult")
else:
    print("Senior Citizen")