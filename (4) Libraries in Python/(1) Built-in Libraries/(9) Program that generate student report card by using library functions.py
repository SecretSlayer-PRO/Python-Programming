# Student Report Card Generator
# Libraries: math, random, datetim

import math         # For mathematical calculations
import random       # For generating roll number
import datetime     # For report date and time

print("         STUDENT REPORT CARD GENERATOR")
# --- datetime library ---
# Get current date and time for the report card
now         = datetime.datetime.now()
date        = now.strftime("%d-%m-%Y")      # Format: Day-Month-Year
time        = now.strftime("%I:%M %p")      # Format: Hour:Min AM/PM
print(f"Date : {date} Time : {time}")

# --- random library ---
# Generate a random roll number
roll_no = random.randint(100, 999)

# --- Input student information ---
name = input("\nEnter Student Name    : ") # \n is used for new line
print("\nEnter Marks for Each Subject (Out of 100):")
marks1 = float(input("    Mathematics : "))
marks2 = float(input("    Physics : "))
marks3 = float(input("    Computer: "))

# Calculate total and percentage
total      = marks1 + marks2 + marks3
percentage = (total / 300) * 100

# --- Selection: Pass or Fail ---
if percentage >= 50:
    status = "PASS "
else:
    status = "FAIL "

# Display Report Card
print("\n          OFFICIAL REPORT CARD")
print(f"  Roll No      : {roll_no}")
print(f"  Name         : {name}")
print(f"  Date         : {date}")
print(f"  Mathematics\t Out of 100 \t {marks1}")   # \t is used for tab
print(f"  Phyiscs\t Out of 100 \t {marks2}")
print(f"  Computer\t Out of 100 \t {marks3:<10}")
print(f"  Total Marks\t Out of 300 \t {total:<10}")
print(f"  Percentage\t {percentage:.2f}%")
print(f"  Status\t {status}")
print("       *** End of Report Card ***")