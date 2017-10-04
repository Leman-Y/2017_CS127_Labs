import math
real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

def encode_letter(letter, r): #letter is letter. r is rotation amount
    newletter=ord(letter)+r
    if ord(letter)+r>122 or ord(letter)+r<97 and letter.islower():
        newletter=(ord(letter)+r)-97
        newletter=newletter%26
        newletter=newletter+97
    elif ord(letter)+r>90 and letter.isupper():
        newletter=(ord(letter)+r)-65
        newletter=newletter%26
        newletter=newletter+65
    return chr(newletter)

print(encode_letter('a',50))
print('\n')

'''
NOTES 10/3/17:
-What went wrong: Whenever the sum of my rotation and ord(letter) was higher than the threshold of the ascii table, I would get a random symbol not letters.
    I needed to use modulus, which allows me to get the letters that I need. Modulus will always be a ratio that is consistent and will never give me a number OVER 26.
    It will stay within the range of 26 and that allows to me to rotate it to the right letter.
1 will be a
27 will be a
53 will be a

2 will be b
28 will be b
54 will be b

1000%26=12
'''
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
print('\n')

'''
Ideas:
-Give out all the distances of the encoded sentences to the the ideal frequency of an English sentence
-Return the rotated encoded sentence that is closest to the one that is an English sentence
'''

def distance(l1,l2):
    """
    Euclidean distance between l1 and l2. If the lists are of 
    different lengths, go to the lenght of the shorter one
    """
    length = len(l1)
    if length>len(l2):
        length = len(l2)
    sum=0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d

def build_frequency_vector(s):
    # count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)

    return v

def compare_rotations(q):
    list1=[]   #lists of the strings' distances to the ideal english sentence
    list2=[]
    for i in range(26):
        #print(encode_string(q,i))
        #print('\n')
        x=(encode_string(q,i))
        c=build_frequency_vector(x)
        #print(distance(real_stats,c))
        v=distance(real_stats,c)
        list1.append(v)
        list2.append(x)
    #print(list1)
     #Get the distanes of all the rotations to the ideal english sentence then append them all into a list
    #print('\n')
    number_closest_to_sentence=0
    #print(min(list1, key=lambda x:abs(x-number_closest_to_sentence)))
    b=list1.index(min(list1, key=lambda x:abs(x-number_closest_to_sentence)))
    #print(b)
    #print(list2)
    print(list2[b])
    
#I was able to make a function that compared all the functions and get the number that was closest to zero. But I want to print the list
    #that was is connected to that zero

#compare_rotations("I have an apple. I have an orange. I have a banana. I have a pineapple")
#print('\n-----------------------------------------------\n')
#compare_rotations("this is a longer sentence with more letters so hopefully it will be closer to the real distribution")
#print('\n-----------------------------------------------\n')

randomstring='Once upon a time, a beautiful princess was locked in the top of a castle. She was guarded by a dragon. There was a reward for saving '\
'the princess. Shrek wanted the reward, so he went to save the princess.'
#print(randomstring)
randomstringencoded=encode_string(randomstring,5)
print(randomstringencoded)
compare_rotations(randomstringencoded)
'''
Notes 10/3/17:
Problems of this decoding is that the function thats that the rotation with the most es is the actual sentence.
'''
'''
s = "I have an apple. I have an orange. I have a banana. I have a pineapple"


r = encode_string(s,3)

print(s)
print(r)

f = build_frequency_vector(s)

print(distance(real_stats,f))

r = encode_string(s,3)

print('/n--------/n')

print(encode_string(s,0))
print(encode_string(s,1))
print(r)
r=build_frequency_vector(r)
print(distance(real_stats,r))
'''