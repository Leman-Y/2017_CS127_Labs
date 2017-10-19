'''
Happy ladybugs
x=2
y=10
c=10
#for i in range(x,y+1):
 #   print(i)

Input example:
4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR

if x<=c<=y:
    print(c)
Notes 10/17/17:
-This is how  you see if a number is in a certain range
-string,b, of length n. ith character  bi, ith cell of board
-If bi is underscore (_), then ith cell of board is empty
-bi is an uppercase alphabet letter (A to Z)
-ith cell has color bi
-String b will not have other characters
-lady bug is happy if left or right cell bi+-1 has another lady bug with same color
-You can move lady bug from its position to empty shell
-n and b for g games
-n= number of cells
-b=string describing n cells

-If there is one ladybug with its own color then return no
-in Q 0-3 are the games
'''
'''
import sys


Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    
def happybug(n,b):
    Happy=('Yes')
    nothappy=('No')
    
    if n==0:
        pass
    if b.count('ABCDEFGHIJKLMNOPQRSTUVWXYZ')==0:
        return Happy

#print(Q)
#print(n)
#print(happybug(0,0))
#print(b)
#print(a0)
print(happybug(1,'A'))
'''
'''
count the letters
if count of letters is not divisible by two then it is not happy so no
'''
'''
I COPIED THIS CODE: (I have no idea how to do this problem
'''
import re

def calculate(n, b):
			  # find if exists any single letter
    if b.count("_") == 0 and len(re.sub(r'((.)\2+)', "", b)) != 0:
        return "NO"
    for a in set(b):
        if a != "_" and b.count(a) == 1:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    b = input()
    print(calculate(n, b))
    