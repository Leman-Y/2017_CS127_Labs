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
    if ord(letter)+r>=122 and letter.islower():
        newletter=newletter-ord('z')+ord('a')-1
    elif ord(letter)+r>=90 and letter.isupper():
        newletter=newletter-ord('Z')+ord('A')-1
    return chr(newletter)

print(encode_letter('A',1))
print(encode_letter('Z',1))
print(encode_letter('a',1))
print(encode_letter('z',1))

'''
I tried to incorporate a function without a function but it did not work.
def encode_string(string,r):
    for letter in string:
        newstring=encode_letter(string,r)
    else:
        newnew=newstring+string
    return newnew
        
print(encode_string('abc1',1))
'''
