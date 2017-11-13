import random
def remove_non_alpha(w):       #rp=remove punctuation but should be name remove_non_alpha
    '''
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    '''
    result=""    #Empty string
    for l in w:  #For the letters in w
        if l.isalpha(): #method isalpha() checks whether the string consists of alphabetic characters only
            result = result + l  #Only keeps the letters
    return result

def dictwords(wordlist):

    '''
    dictwwords=key with words and words after
    input: list of words
    output: Dictionary of keys with words and values of words after the word
    '''

    d={}         #Empty dic
    
    for w in range(len(wordlist)-1): #For word in l, the list
        #print(w)
        d.setdefault(wordlist[w],list()) #Set the keys in the dictionary the index of the word in the wordlist
        #in set.default(a,b)  a is the key, b is the value for the key
        d[wordlist[w]].append(wordlist[w+1])
    d.setdefault(wordlist[-1])
    

    '''
    for i in range(0,len(wordlist)-1):
        d.setdefault(wordlist[i],list())
        d[wordlist[i]].append(wordlist[i+1])
    '''

    #for k in d:
    #    print(k)
    return d            #Returns the frequency of the word in the list


def bwcff(f):        #f is file name then f is the content of the file so change it
    '''
    bwcff=build word count from file
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
            of the number of times each word occurs
    '''
    text = open(f).read()  #Opens the text
    l=[]                #Make an empty list
    for w in text.split(): #For words in the text split it
        w = w.lower()   #Turn the words into the lowercase version of the word
        w = remove_non_alpha(w)       #rp is the function on top
        l.append(w)    #Append the rp(w) to the empty list
    #print(l)
    d = dictwords(l)        #Put l into the function bwcd and call the variable d
    return d

#d = bwcff("hamlet.txt")

#print(bwcff('hamlet.txt'))

def bigrams(wordlist):

    '''
    dictwwords=key with words and words after
    input: list of words
    output: Dictionary of keys with words and values of words after the word
    
    '''
    d={}         #Empty dic
    
    for w in range(len(wordlist)-1): #For word in l, the list
        #print(w)
        x=wordlist[w],wordlist[w+1] #Set a variable for w and w+1
        d.setdefault(x,list()) #Set the keys to x
        #in set.default(a,b)  a is the key, b is the value for the key
        #d[wordlist[w]].append(wordlist[w+1])
        if w<(len(wordlist)-2):
            d[x].append(wordlist[w+2])

    

    return d            #Returns the frequency of the word in the list

def bwcff1(f):        #f is file name then f is the content of the file so change it
    '''
    bwcff=build word count from file
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
            of the number of times each word occurs
            
    FOR BIGRAMS BIGRAMS BIGRAMS BIGRAMS BIGRAMS BIGRAMS BIGRAMS 

    '''
    text = open(f).read()  #Opens the text
    l=[]                #Make an empty list
    m=[] #make new list to filter out empty string
    for w in text.split(): #For words in the text split it
        w = w.lower()   #Turn the words into the lowercase version of the word
        w = remove_non_alpha(w)       #rp is the function on top
        l.append(w)    #Append the rp(w) to the empty list
    #print(l)
    
    for word in l:
        if len(word)>=1:
            m.append(word)
    '''
    m=[]
    Making a new list that takes out the empty strings of the original list helps us out
    '''
    
    d = bigrams(m)        #Put l into the function bwcd and call the variable d
    return d

print(bwcff1('hamlet.txt'))

x={}
s=['a','b','c','d','e']

for w in range(len(s)-1):
    d=s[w],s[w+1]
    x.setdefault(d)
#print(x)
    
def generate_text(d,start_word,length=50):
    '''
    #Make a sentence of words which are randomly chosen 
    '''
    wordlist=[]
    next=start_word
    for i in range(length):
        if next not in d:
            break
        wordlist.append(next)
        next=random.choice(d[next])
    return (wordlist)


hamlet=bwcff1('hamlet.txt')
psalms=bwcff1('psalms.txt')
sonnets=bwcff1('sonnets.txt')
#print(generate_text(hamlet,('to'),10))

'''
Notes 11/12/17:
-Not working
-generate_text is not working
-It is not taking in the value in the key
print(hamlet[('to', 'be')][0])

hamlet=bwcff('hamlet.txt')
psalms=bwcff('psalms.txt')
sonnets=bwcff('sonnets.txt')
#print(bwcff('hamlet.txt'))
#print(generate_text(hamlet,'to',20))
'''

print('\n------------------------------------------------------------------------------\n')

def trigrams(wordlist):

    '''
    dictwwords=key with words and words after
    input: list of words
    output: Dictionary of keys with words and values of words after the word
    
    '''
    d={}         #Empty dic
    
    for w in range(len(wordlist)-2): #For word in l, the list
        #print(w)
        x=wordlist[w],wordlist[w+1],wordlist[w+2] #Set a variable for w and w+1
        d.setdefault(x,list()) #Set the keys to x
        #in set.default(a,b)  a is the key, b is the value for the key
        #d[wordlist[w]].append(wordlist[w+1])
        if w<(len(wordlist)-3):
            d[x].append(wordlist[w+3])

    

    return d            #Returns the frequency of the word in the list

def bwcff2(f):        #f is file name then f is the content of the file so change it
    '''
    bwcff=build word count from file
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
            of the number of times each word occurs
            
    FOR TRIGRAMS TRIGRAMS TRIGRAMS TRIGRAMS

    '''
    text = open(f).read()  #Opens the text
    l=[]                #Make an empty list
    m=[]
    for w in text.split(): #For words in the text split it
        w = w.lower()   #Turn the words into the lowercase version of the word
        w = remove_non_alpha(w)       #rp is the function on top
        l.append(w)    #Append the rp(w) to the empty list
    #print(l)
    for word in l:
        if len(word)>=1:
            m.append(word)
    d = trigrams(m)        #Put l into the function bwcd and call the variable d
    return d

print(bwcff2('hamlet.txt'))
