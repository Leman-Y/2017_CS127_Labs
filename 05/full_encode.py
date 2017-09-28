'''
Write a routine full_encode(s) which takes a string and returns a string representing all the valid rotations,
one per line (embed the \n to get a newline).

I want to create a loop where I rotate the string by the length of itself. So if the string has a length of 3. I want
to rotate it 1,2,3 times and have all that print out.
'''
import collections

def full_encode(s):
    s=collections.deque(s)
    for i in range(len(s)):
        s.rotate(i)
        print(s)

print(full_encode('abc'))
print(full_encode('abcd'))
'''
import collections

def full_encode(s):
    s=collections.deque(s)
    s.rotate(3)
    return s
print(full_encode('abc'))

abc
bca
cab
'''