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


"""
Coding question 2:💻
The distance between two cities (in km) is input through keyboard. Write a program to
convert and print the distance in meters, feet, inches and centimetres.
"""

kmDist = int(input("Enter distance between two cities (in km): "))
mDist = kmDist*1000
cmDist = mDist*100
ftDist = kmDist*3280.84
inchDist = ftDist*12
print(f"\nDistance in meters {':':>8} {mDist} m\
\nDistance in feet {':':>10} {ftDist} ft\
\nDistance in inches {':':>8} {inchDist} in\
\nDistance in centimeters {':':>3} {cmDist} cm")
