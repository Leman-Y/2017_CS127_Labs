'''
def ap(x):
    we=('No')
    qw=('Yes')
    if x==1:
        return qw
    elif x!=1:
        return we

#print(ap(1))
print(ap(100))
print(len('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
'''

def freq(n,l):
    frequency=0
    for number in l:
        if number==n:
            frequency+=1
    return frequency

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
    #print(q[])
    #print(q[2])
    #print('\n')
    for g in q:
        #print(g)
        if r<g: #r=1 but 1 is less than 2 so r should be 2 now not 1
            r=g
            #print(q.index(r))
            x=q.index(r)
            

    return l[x]      #saveg
   

u=[1,2,3,4,5,10,10]
print(mode2(u))
t=[1,2,3,4,4,4]
print(mode2(t))

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
'''
'''
'''
'''
b='ABCDEFGHIJKLMNOPQRSTUVWXYZAPPLE'
#print(b.count('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
ce='APPLE'
print(b.count('c'))
print(b.count('ce'))
'''
'''
b.count wont use the variable c 
'''


