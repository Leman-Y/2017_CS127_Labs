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

def bwcd(wordlist):
    d={}         #Empty dic
    for w in wordlist: #For word in l, the list
        d.setdefault(w,0)  #
        d[w] = d[w] + 1
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
    d = bwcd(l)        #Put l into the function bwcd and call the variable d
    return d

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
d = bwcff("hamlet.txt")


print(bwcff('hamlet.txt'))
#print(remove_non_alpha('.w'))
#print(bwcd(['apple','apple','orange']))

v=d.values()
#print(v)
v=list(d.values())
#print(v)
#print(v.sort())
'''
d2=bwcff('sonnets.txt')
v2=list(d2.values())
for l in d2:
    if d2[l]>150:
        print(l,':',d2[l])
'''        
#sum(v2) total number of words
'''
l=[]
for a in b:
    if ___:
        l.append(__)
____________________
l=[]
for k in d:
    if ____:
        l.append(___)

'''
l=[x for x in range(10)]
l
'''
this equals to
l=[]
for x in range(1):
    (.append(x))
'''
'''
[l for l in 'hello world']

numbers=[1,2,3,10,20,30]
print([x**x for x in numbers])

d={'a':5,'b':10,'c':20}
print([k for k in d])
print([d[k] for k in d])

print([k for k in d2 if d2[k]>200])
#d2 was the sonnts
#Only give me the k if d sub 2 is greater than 200
print([k.upper() for k in d2 if d2[k]>200])
print([k.upper() for k in d2 if d2[k]>50 and d2[k]<100])

print([(x,y) for x in range(4) for y in range(5)])
'''
'''
-Word counts are interesting because you can do sentiment analysis
-You can see positive or negatives
-See the similariities between articles
'''