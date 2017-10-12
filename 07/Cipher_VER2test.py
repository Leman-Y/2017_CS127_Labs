def build_frequency_vector2(s):
    v=[]
    for letter in s:
        if letter.lower() in 'qwertyuioplkjhgfdsazxcvbnm':
             v.append(letter)
    print(len(v))
    print(v)
    
x='abcdefg.()'
c='ABCDEFGz.()'
b='abcdefghijklmnopqrstuvwxyz.()'
n='abcdefghijklmnopqrstuvwxyz'
v=c.lower()
#print(v)
#build_frequency_vector2(x)
#build_frequency_vector2(c)

def build_frequency_vector(s):
    # count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)
    #what does s.count(letter) do?
    return v

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
    print(v)
    return v
(build_frequency_vector3(c))
#abcdefghijklmnopqrstuvwxyz
def abc(x):
    x=3
    d=4
    return x,d
#print(abc(5))
'''
Notes 10/11/2017:
-Build frequency vector:
    -I had a problem where I had two returns and it would not work. So I guess I just need to use print or do not use return at all, which ...
    -is what I did. I got an empty list, then for every letter in s(string) if the character is in the lower case alphabet then it would ...
    -add that letter to q. This allows me to remove all the punctuation and strictly have letters. Then I made all the letters which were ...
    -upper case to lower case. I turned the list into a string with (''.join()). I counted the length of the letters, then individually ...
    -divided each letter by the total length of the string.
-FUNCTIONS BREAK ON FIRST RETURN
'''
#print(build_frequency_vector(x))
#print(build_frequency_vector(c))
#print(build_frequency_vector(b))
#print(build_frequency_vector(n))
