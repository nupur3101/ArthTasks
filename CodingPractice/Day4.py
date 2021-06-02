# June 2, 2021

"""
Coding question 5:

Create the Swastika Pattern

*     * * * * 
*     *       
*     *       
* * * * * * *
      *     * 
      *     * 
* * * *     *

"""

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
for i in range(r):
    for j in range(c):
        if i < r//2:
            if j < c//2:
                if j == 0 :
                    print("* ", end="")
                else :
                    print(" ", end=" ")
            elif j >= c//2:
                if i == 0:
                    print("* ", end="")
                else:
                    if j == c//2:
                        print("* ", end="")
        elif i == r//2:
            print("* ", end="")
        else :
            if j == c//2 or j == c-1:
                print("* ", end="")
            elif i == r-1 and j < c//2:
                print("* ", end="")
            else:
                print(" ",end=" ")
    print()
