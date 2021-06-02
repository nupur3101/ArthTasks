# 30/05/2021

"""
Coding question 1:💻
Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% 
of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.
"""

basicSal = int(input("Enter basic salary : "))
dearanceAllowance = 0.40
houseRentAllowance = 0.20
GrossSal = basicSal + (dearanceAllowance*basicSal) + (houseRentAllowance*basicSal)
print("Gross Salary : ",GrossSal)
