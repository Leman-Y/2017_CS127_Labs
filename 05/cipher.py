'''
Write a routine encode_letter(c,r) which takes a letter (a-z) and returns a letter that is it rotated by r positions.
So, rotate_letter('a',3) would return 'd' and roate_letter('y',3) would return 'b'.

def rotateletter(l,n) #l is letter and n is rotation

This code was copied for reference. I had no idea where to start and how to get from z to a in python.

def alphabet_position(letter, number):
    if len(letter) != 1:
        return -1 #Invalid input
    elif letter.isalpha() == False:
        return letter #If its not an alphabet
    else:
        ans = ord(letter) + number
        # the below if-statement makes sure the value does not overflow.
        if ans > ord('z') and letter.islower():
            ans = ans - ord('z') + ord('a')-1
        elif ans > ord('Z') and letter.isupper():  
            ans = ans - ord('Z') + ord('A')-1
        return chr(ans)
print(alphabet_position('y',2))
'''
def encode_letter(letter, r): #letter is letter. r is rotation amount
    newletter=ord(letter)+r
    if ord(letter)+r>122 and letter.islower():
        newletter=newletter-ord('z')+ord('a')-1
    elif ord(letter)+r>90 and letter.isupper():
        newletter=newletter-ord('Z')+ord('A')-1
    return chr(newletter)

print(encode_letter('A',1))
print(encode_letter('Z',1))
print(encode_letter('a',1))
print(encode_letter('z',1))
print(encode_letter('a',25))
print(encode_letter('A',25))
print('\n')


def encode_string(string,r):
    result=''
    for letter in string:
        if letter.lower() in 'qwertyuioplkjhgfdsazxcvbnm':
            result+=encode_letter(letter,r)
            #result=encode_letter(letter,r)
            #result=''+encode_letter(letter,r)
            #result+=encode_letter(letter,r)==result=result+encode_letter(letter,r)
            #result+= means that you add the letters to each other. so if string is'abc'. a is changed then puts in an empty box. b is changed and is added to changed a. etc
        else:
            result += letter
    return result
print(encode_string('abc1',1))
print(encode_string('abc1',25))
#it will end for loop prematurely if you put return in for loop
print('\n')

'''
def encode_string2(string,r):
    result=''
    for letter in string:
        if ord(letter) in range(65,91) or ord(letter) in range(97,123):
            #not in range(ord(65),ord(91)) because if ord(letter) already translates the ord. SO by doing ord(65) you get another value in the ascii system.
            #ord('1')=49
            result+=encode_letter(letter,r)
        else:
            result+=letter
    return result

print(encode_string2('abc1',1))
print(encode_string2('abcd1',1))
'''

def full_encode(s):
    for i in range(26):
        print(encode_string(s,i) + "\n")
        
full_encode('abcd1')
print('\n')
#full_encode('xyz')

'''
NOTES:
I tried to incorporate a function without a function but it did not work.
def encode_string(string,r):
    for letter in string:
        newstring=encode_letter(string,r)
    else:
        newnew=newstring+string
    return newnew
        
print(encode_string('abc1',1))

NOTES: 10/1/16
- So my problem for full encode was that when I rotate a 25 times it would get ` instead of z. I knew I messed up. Encode letter had to be > ord(z)
    not >= ord(z)
-This fixed my problem
-I did print(full_encode(___)), which gave me none in the end which was not needed. I just had to do full_encode, because in my function it already says print.
    so doing print(full_encode(___)) is redundant and gives me the none as well.
-RANGE(X) DOES NOT INCLUDE X BUT X-1. EXCLUSIVE
'''

