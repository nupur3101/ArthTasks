# June 1, 2021

"""
Coding question 4:
Program to accept three numbers from user and print them in ascending and decending order
"""

# Solution 1
x = list(map(int,input("Enter three numbers : ").strip().split(" ")))

while True:
    print("\nPress 1 to print in ascending order\
    \nPress 2 to print in descending order")
    ch = int(input("Enter your choice : "))
    if ch==1 :
        x.sort()
        print("\nAscending order : ")
        break
    elif ch==2 :
        x.sort(reverse=True)
        print("\nDescending order : ")
        break
    else:
        print("!! Please enter correct choice !!\n")
for i in x:
    print(i, end=' ')
    
    
# Solution 2
x = list(map(int,input("Enter three numbers : ").strip().split(" ")))
print("Ascending order : ",sorted(x))
print("Descending order : ",sorted(x, reverse=True))
