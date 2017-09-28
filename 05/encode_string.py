'''
Write a routine encode_string(s,r) which return a new string which is the original string with each letter rotated.
It should not rotate non-letters, those should just be copied over to the new string. Upper case letters should be rotated.
You can convert them to lower case, rotate then convert back or you could make your rotate_letter routine handle it directly.
'''
import collections

def encode_string(string,r):
    string=list(string) #not necessary
    string=collections.deque(string)
    string.rotate(r)
    string=list(string)
    return string

print(encode_string('abc',1))
print(encode_string('abcd',2))
print(encode_string('abc1',1))
'''
My code does fulfill the conditions to rotate nonletters. I do not know how to isolate the nonletters then add the back to the end of the string.
def encode_string(string,r):
    string=list(string)
    string=collections.deque(string)
    string.rotate(r)
    if any(char.isdigit() for char in string)
    return string
'''