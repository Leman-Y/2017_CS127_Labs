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
    #d = dictwords(l)        #Put l into the function bwcd and call the variable d
    return l

d = bwcff("hamlet.txt")
#print(d)

def bwcff_test(f):        #f is file name then f is the content of the file so change it
    '''
    bwcff=build word count from file
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
            of the number of times each word occurs
    '''
      #Opens the text
    l=[]                #Make an empty list
    m=[] #make new list to filter out empty string
    for w in f.split(): #For words in the text split it
        w = w.lower()   #Turn the words into the lowercase version of the word
        w = remove_non_alpha(w)       #rp is the function on top
        l.append(w)    #Append the rp(w) to the empty list
    print(l)
    for word in l:
        if len(word)>=1:
            m.append(word)
    #print(l)
    #print(m)

                

            
    #print(l)
    d = dictwords(l)        #Put l into the function bwcd and call the variable d
    return d

x='And lose the name of action. -- Soft you now, The fair Ophelia! -- Nymph, in thy orisons'
print(bwcff_test(x))
