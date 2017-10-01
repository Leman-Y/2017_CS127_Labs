'''
Write a routine encode_string(s,r) which return a new string which is the original string with each letter rotated.
It should not rotate non-letters, those should just be copied over to the new string. Upper case letters should be rotated.
You can convert them to lower case, rotate then convert back or you could make your rotate_letter routine handle it directly.
'''
'''
THIS FILE DOES NOT WORK
'''
import collections

def encode_string(string,r):
    string=list(string) #not necessary
    string=collections.deque(string)
    string.rotate(r)
    string=list(string)
    str1=''.join(string)
    return str1

print(encode_string('abc',1))
print(encode_string('abc',2))
print(encode_string('abcd',2))
print(encode_string('abc1',1))

#USE ENCODE LETTER IN ENCODE STRING
#this does not work, because it does not give you the next letter, but it rotates the order
def encode_letter(string,r):
    result=''
    for letter in string:
        if ord(letter) in range(65,91) or ord(letter) in range(97,123):
            result+=encode_string(letter,r)
    else:
        result+=letter
    return result

print(encode_letter('abc',1))
'''
result=''
result+=''
result=result+''



My code does fulfill the conditions to rotate nonletters. I do not know how to isolate the nonletters then add the back to the end of the string.
def encode_string(string,r):
    string=list(string)
    string=collections.deque(string)
    string.rotate(r)
    if any(char.isdigit() for char in string)
    return string
    
NOTES 10/1/17:
-This moved the order of the string. This did not rotate a letter n times and give back a new letter. I had to make a new program.

'''