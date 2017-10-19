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
    
