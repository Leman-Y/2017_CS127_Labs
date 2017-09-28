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
#but if i do return(s) it does not rotate for me. it does rotate 1 and 3 but not 2.
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

This code works for the video but not here for some reason

import string
import collections

def caesar(rotate_string,number_to_rotate_by):
    upper=collections.deque(string.ascii_uppercase)
    lower=collections.deque(string.ascii_lowercase)
    
    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)
    
    upper=''.join(list(upper))
    lower=''.join(list(lower))
    
    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))


print (caesar('This is too easy',1))
'''