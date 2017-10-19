'''
s=[1,2,3,4,5]
for i in s:
    print(i)
'''
#d= units of diance d+ to the right d- to the left
#determine apples fallen on inclusive range [s,t]
#print('Input distance of s & t')
#input=()

#m= apples & n=oranges
#m has integers of each distance the apple falls from the tree & n has integers of each distance the apple falls from the tree
'''
So we got a set of inputs 1st-5th line

s,t= the inclusive range of the house s,t
a,b= (a=where the apple tree is located)(b=where the orange tree is located)
m,n= (m=number of apples, n=number of oranges)
m[list]= distance of where each apple falls
n[list]=distance of where each orange falls

apple=0
if a+d in range of [s,t]
    apple+=1
    print(apple)
    
orange=0
if b+d in range of [s,t]
    orange+=1
    print(orange)

def countFruits():

#I want to turn each distances of the apples and orange, and where they fall into a list
numberofapples=0
for x in apple: #x is distance of apple that falls from tree
    if a+x in range of (s,t]):
        numberofapples+=1
    print(numberofapples)

numberoforanges=0
for c in orange:
    if a+c in range of (s,t):
        numberoforanges+=1
    print(numberoforanges)
    

  
apples=[5,7,9]
oranges[10, 11]
int a=
int b=
int s=
int t=
countFruits(apples, a, b, s, t)

apples=[5,7,9]
oranges=[10, 11]
def countfruits(apples,oranges):
    print(apples)
    print(oranges)
countfruits(apples,oranges)
'''


import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
    
#apple and orange are the distances of each apple and orange away from their tree
numberofapples=0
for item in apple:
    if s<=item+a<=t:
        numberofapples+=1
print(numberofapples)
    #print(item)
#print('\n')
#print(range(s,t))
#print(apple)
numberoforanges=0
for item in orange:
    if s<=item+b<=t:
        numberoforanges+=1
print(numberoforanges)


'''
7 11
5 15
3 2
-2 2 1
5 -6
Should get:
1
1

1 2
0 3
3 3
1 1 1
-1 -1 -1
Should get:
3
3
'''