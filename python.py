"""Task
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird
 """
code:
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
if n%2!=0 :
    print("Weird")
elif n%2==0 and n in range(2,6) :
    print("Not Weird") 
elif n%2==0 and n in range(6,21) :
    print("Weird")
else:
    n%2==0 and range(20<n) 
    print("Not Weird")            

