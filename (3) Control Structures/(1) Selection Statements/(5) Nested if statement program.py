# This is a nested if statement program
age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

if age >= 18:
    print("Age requirement met.")
    if salary >= 30000:
        print("Salary requirement met.")
        print("Loan APPROVED!")
    else:
        print("Salary too low")
        print("Loan REJECTED!")
else:
    print("Age requirement not met.")
    print("Loan REJECTED!")