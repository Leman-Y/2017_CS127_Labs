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
'''
def bwcd(wordlist):
    d={}         #Empty dic
    for w in wordlist: #For word in l, the list
        d.setdefault(w,0)  #
        d[w] = d[w] + 1
    return d            #Returns the frequency of the word in the list

'''

'''
Notes:
-Frequency of the keys
-How long the word appears
-Change the variable into something you know
-Function names themselves probably not the best name
-You can do help(remove_non_alpha) to help you
-Input and output
-Put a string into the function called the doc string to help you put
'''


#print(bwcff('hamlet.txt'))
'''
---------------------------------------------
'''
'''
HOMEWORK DUE THURSDAY 10/9/17:
-Make a dictionary with the keys and a list in each key
-The key will have a list of words that follow the key
-'to':['be','be'
-'be':['or','that'
-'or':['not'
'''
'''
def dictwords(wordlist):
    d={}
    for w in range(len(wordlist)-1):
        d.setdefault(wordlist[w],'')
        d[wordlist[w]]=''+str(wordlist[w+1])
    d.setdefault(wordlist[-1])
    
    return d
    
print(dictwords(['a','b','c','a','d']))
#This does not work for some reason. The words that come after one specific word are not shown just one word
'''

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
    print(l)
    d = dictwords(l)        #Put l into the function bwcd and call the variable d
    return d

#d = bwcff("hamlet.txt")

print(bwcff('hamlet.txt'))

'''
PROBLEMS:
-If the word is repeated. The word will not be recorded
-Does zamansky want multiple keys if they are the same word?
-d{'to':none,'to':none}
-d.setdefault(wordlist[w]) when I do this. Multiple keys of the same word are not created but just one key of one specfic name
-In a dict you cannot add multiple forms of the same word. No multiple keys

'''
x=['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question', 'whether', 'tis', 'nobler', 'in', 'the', 'mind', 'to', 'suffer', 'the', 'slings', 'and', 'arrows', 'of', 'outrageous', 'fortune', 'or', 'to', 'take', 'arms', 'against', 'a', 'sea', 'of', 'troubles', 'and', 'by', 'opposing', 'end', 'them', 'to', 'die', 'to', 'sleep', 'no', 'moreand', 'by', 'a', 'sleep', 'to', 'say', 'we', 'end', 'the', 'heartache', 'and', 'the', 'thousand', 'natural', 'shocks', 'that', 'flesh', 'is', 'heir', 'to', 'tis', 'a', 'consummation', 'devoutly', 'to', 'be', 'wished', 'to', 'die', 'to', 'sleep', 'to', 'sleepperchance', 'to', 'dream', 'ay', 'theres', 'the', 'rub', 'for', 'in', 'that', 'sleep', 'of', 'death', 'what', 'dreams', 'may', 'come', 'when', 'we', 'have', 'shuffled', 'off', 'this', 'mortal', 'coil', 'must', 'give', 'us', 'pause', 'theres', 'the', 'respect', 'that', 'makes', 'calamity', 'of', 'so', 'long', 'life', 'for', 'who', 'would', 'bear', 'the', 'whips', 'and', 'scorns', 'of', 'time', 'th', 'oppressors', 'wrong', 'the', 'proud', 'mans', 'contumely', 'the', 'pangs', 'of', 'despised', 'love', 'the', 'laws', 'delay', 'the', 'insolence', 'of', 'office', 'and', 'the', 'spurns', 'that', 'patient', 'merit', 'of', 'th', 'unworthy', 'takes', 'when', 'he', 'himself', 'might', 'his', 'quietus', 'make', 'with', 'a', 'bare', 'bodkin', 'who', 'would', 'fardels', 'bear', 'to', 'grunt', 'and', 'sweat', 'under', 'a', 'weary', 'life', 'but', 'that', 'the', 'dread', 'of', 'something', 'after', 'death', 'the', 'undiscovered', 'country', 'from', 'whose', 'bourn', 'no', 'traveller', 'returns', 'puzzles', 'the', 'will', 'and', 'makes', 'us', 'rather', 'bear', 'those', 'ills', 'we', 'have', 'than', 'fly', 'to', 'others', 'that', 'we', 'know', 'not', 'of', 'thus', 'conscience', 'does', 'make', 'cowards', 'of', 'us', 'all', 'and', 'thus', 'the', 'native', 'hue', 'of', 'resolution', 'is', 'sicklied', 'oer', 'with', 'the', 'pale', 'cast', 'of', 'thought', 'and', 'enterprise', 'of', 'great', 'pitch', 'and', 'moment', 'with', 'this', 'regard', 'their', 'currents', 'turn', 'awry', 'and', 'lose', 'the', 'name', 'of', 'action', '', 'soft', 'you', 'now', 'the', 'fair', 'ophelia', '', 'nymph', 'in', 'thy', 'orisons', 'be', 'all', 'my', 'sins', 'remembered']

print(x[0])
print(x[274])
print(x[275]) #275 is remebered but is not shown in the dictionary
#print(x[276]) #out of range
'''
{'to':'be','suffer','or':'not','not':'to'}
'''
