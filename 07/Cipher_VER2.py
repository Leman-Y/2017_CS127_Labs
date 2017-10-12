import math
f=open('Tom-Sawyer.txt')
s=f.read()
f.close()
#print(s)

def build_frequency_vector3(s):
    q=[]
    for letter in s:
        if letter.lower() in 'qwertyuioplkjhgfdsazxcvbnm':
             q.append(letter)
    #print(q)
    w=[w.lower() for w in q]
    #print(w)
    e=''.join(w)
    #print(e)
    num_letters=len(e)
    #print(len(e))
    v=[]
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        v.append(e.count(letter) / num_letters)
    #print(v)
    return v
#letter.lower() in
#x='APple got it. Yea boy. '
#(build_frequency_vector3(x))

print(build_frequency_vector3(s))
real_stats=build_frequency_vector3(s)
print('\n--------------------\n')

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

#print(encode_letter('a',50))
#print('\n')

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
#print(encode_string('abc1',1))
#print('\n')

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
#ZAMANSKY NEEDS TO EXPLAIN THIS AGAIN
#x='abcdefghijklmnopqrstuvwxyz'
#c=build_frequency_vector3(x)
#print(c)
#print(distance(real_stats,c))
#x=[3,10]
#c=[2,8]
#print(distance(x,c))
'''
Notes:
- Upper case letters would not work
    -when I do this: for letter in "abcdefghijklmnopqrstuvwxyz" or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
-I fixed it in my test
'''
def compare_rotations(q):
    list1=[]   #lists of the strings' distances to the ideal english sentence
    list2=[]
    for i in range(26):
        #print(encode_string(q,i))
        #print('\n')
        x=(encode_string(q,i))
        c=build_frequency_vector3(x)
        #print(distance(real_stats,c))
        v=distance(real_stats,c)
        list1.append(v)
        list2.append(x)
    #print(list1)
    #print('\n')
     #Get the distanes of all the rotations to the ideal english sentence then append them all into a list
    #print('\n')
    number_closest_to_sentence=0
    #print(min(list1, key=lambda x:abs(x-number_closest_to_sentence)))
    b=list1.index(min(list1, key=lambda x:abs(x-number_closest_to_sentence)))
    #print(b)
    #print(list2)
    #print('\n')
    print(list2[b])
    
def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i]," : ",v[i])
        
'''
NOTES 10/11/17:
-I am trying to build 'build_frequency_vector2(s)' that just takes the letter from the Tom Sawyer book and gives me the frequency of it. How many time it appears as
    a letter divided by the total sum of the letters.
'''
randomstring='Once upon a time, a beautiful princess was locked in the top of a castle. She was guarded by a dragon. There was a reward for saving '\
'the princess. Shrek wanted the reward, so he went to save the princess.'
#print(randomstring)
randomstringencoded=encode_string(randomstring,5)
#print(randomstringencoded)
compare_rotations(randomstringencoded)

tomsawyer='The old lady pulled her spectacles down and looked over them about the room; then she put them up and looked out under them.'
tomsawyerencoded=encode_string(tomsawyer,6)
#print(tomsawyer)
#print(tomsawyerencoded)
compare_rotations(tomsawyerencoded)