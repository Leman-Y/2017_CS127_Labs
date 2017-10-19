'''
how_many.py: has these functions
1.freq(n,l) which will be passed a list of integers l and a single integer n.
    It will return the frequency of which l appears, that is how many times it appears.
    So, freq(3,[3,2,2,1,3,4,5,4,3,4,3]) would return 4 since 3 appears 4 times.
    DO NOT USE COUNT -- loop through the list and do this manually.
2.min(l) -- calculates the smallest value of the list - again,
    do this manually using a loop not using a built in function.
3.mode(l) which returns the mode - the most frequently occurring item in the list -
    you can assume a single mode in the list, that is there wont be two items that appear the most times.
'''
def freq(n,l):
    frequency=0
    for number in l:
        if number==n:
            frequency+=1
    return frequency

x=[1,2,3,4,5,5,3]
b=5
print(freq(b,x))
print('\n')

def min(l):
    min=l[0]
    for number in l:
        if number<min:
            min=number
    return min
x=[1,2,3,4,5,5,3,.5,.2]
print(min(x))
print('\n')

'''
I copied mode1 from online. I imported a module which helped me find the mode.
However this module will give an error if there are two numbers that have the same mode in a list
'''

from statistics import mode
def mode1(l):
    x=mode(l)
    return x
    
y=[1,2,3,4,5,2]
print(mode1(y))
#u=[1,2,3,4,5,2,1,1]
#print(mode1(u))
print('\n')

def mode2(l):
    #How do I personally find the mode myself? I see which numbers frequently appear, then count the amount they appear in.
    q=[]
    for number in l:
        x=freq(number,l)
        q.append(x)
        #print(number)
    print(q)
    #x=q[0]
    #print(x)
    #print(min(q))
    #c=q.index(min(q))
    #print(c)
    r=q[0]
    #print(r)
    #print(number)
    #print(q[1])
    #print(q[2])
    #print('\n')
    for g in q:
        #print(g)
        if r< q[g]: #r=1 but 1 is less than 2 so r should be 2 now not 1
            r=l[g]
    return r
    print(r)

u=[1,2,3,4,5,10,10]
print(mode2(u))
'''
HW HELP:
-For some reason in mode2 in the second for loop I try to get the highest number, which would be the one that is the mode...
-But instead the function gives me one. The mode is 10 for list u. If the r=q[0] which is 1 and 1 is less than q[g] at 5,6 then I should...
-get back 2 but I do not.
'''
'''
THIS SHOULD REMOVE EVERYTHING BUT IT DOESNT
'''
        #print(v)
        #low=q[0]
        #if v>min(q):
            #q.remove(min(q))
            #low=v
    #print(q)

'''
Notes 10/11/17:
-The numbers between [2,1,1,2] will not be removed. I am trying to remove all lowest minimum numbers in the list q, so I get all the highest number ...
    - or all the frequencies of them. 
'''
    #print(min(q))
    #print(q)
            
    #if min(q)<x:
     #   c=min(q)
      #  q.remove(c)
    #print(q)
        
    #print(q[5])
    #print(number)
    #print(q[number])
    #e=q[number]
    #print(e)
    #print(number)
    #for i in q:
    #    if e<q[i]: 
     #       q.remove(e)
     #       e=q[i]
    #print(q)
    #print(l)
    #print(min(q))
    #print(min(l))


