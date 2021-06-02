# May 31,2021

"""
Q.3 Draw this Pattern 👇
    *
   * * 
  * * *
 * * * *
* * * * *
"""

# Solution 1
p = int(input("Enter an integer: "))
print()
for i in range(1,p+1):
    print(" "*(p-i),"* "*i)
    
    
# Solution 2
p = int(input("Enter an integer: "))
for i in range(p):
    for j in range(2*p-1):
        if j < p-i-1 or j > p-i-1:
            print(" ", end="")
        else:
            print("* "*(i+1),end="")
    print()
