some_list = ["apple", "pear", "banana", "grape"]
#print(some_list.index("pear"))

#print(some_list.index("grape"))
#some_list.remove(1)
'''
def freq(n,l):
    frequency=0
    for number in l:
        if number==n:
            frequency+=1
    return frequency
'''
'''
def mode2(l):
    #How do I personally find the mode myself? I see which numbers frequently appear, then count the amount they appear in.
    q=[]
    for number in l:
        q.append(freq(number,l))
        #print(number)
    print(q)

u=[2,3,4,5,6,3]
mode2(u)
'''
def freq(n,l):
    frequency=0
    for number in l:
        if number==n:
            frequency+=1
    return frequency

def mode2(l):
    q=[]
    for number in l:
        x=freq(number,l)
        q.append(x)
    r=q[0]
    for g in q:
        if r< q[g]: 
            r=l[g]
    print(r)
u=[1,2,3,4,5,10,10]
mode2(u)

