
import csv
'''
Assignment:
Create an inverted index as specified in class and test it by entering
words and printing out which documents or statements  (from
offenders-cleaned.csv) contain those words.

NOTE THAT I REFERENCED MY CODE FROM JASON
'''

'''
reader=csv.reader(open('sample.csv'))
for line in reader:
    print (line)
    
reader=csv.reader(open('offenders.csv'))
print(reader)
'''
'''
for row in reader:
    print (row)
'''
'''
what does python set do?

Notes 11/15/17:
-I have no idea what to do
-I cannot read the offenders.csv file from thonny for some reason
-'I keep on getting the error utf-8' codec can't decode byte 0x89 in position 1016: invalid start byte'
-Is the file too large?

Plan:
-Get each line from the offenders.csv file. Each line would be each offender and his/her statement
-[8]- would be the statement
-Create function that will remove the unneccesary punctuation
-Create program that will allow you to put a word. And that word will show you which offender has that word in his statement.

'''
f = open('sample-texts.csv')
csv_reader = csv.reader(f)
l = []
for line in csv_reader:
    l.append(line)
f.close()
    
print(l)

def removepunc(string):
    '''
    Input: A string
    Output: Just a string with letters and no punctuation
    Example: '.'.isalpha() is false
    '''
    empstr=''   #emptystring
    for char in string:
        if char.isalpha()==True or char==' ': #char==' ' includes a space
            empstr+=char
    return empstr.split()  #Split the string into words 

#print(removepunc('abcd.l.,;'))

def invertedindex(file):
    '''
    Input: Any csv file
    Output: Dictionary of statements
    '''
    f=open(file)
    csv_reader=csv.reader(f)
    l=[] #Empty list
    for line in csv_reader:
        l.append(line)
    f.close()
    #Here we have list of lists
    d={} #Empty dictionary
    for eachlist in l: #Each offender has a line
        statement=removepunc(eachlist[8]) #This is the statement of each offender. And you want to apply removepunc
        for word in statement: #Each word in statement
            d.setdefault(word, []) #Create a dictionary with keys of the word and a empty list in those keys
            if eachlist[3] not in d[word]: #If the prisoner number is not in the word
                d[word].append(eachlist[3]) #Add the prisoner number to each word
    return d 

def inputword(word):
    '''
    Input: Word
    Output: Which prisoner statement has that word
    '''
    for w in prisonernumbers: #w==word
        if w==word:
            return prisonernumbers[w] #Will return the prisonersnumbers that have the words in his/her statement
    

def invertedindex1(file, word):
    '''
    Input: Any csv file and a word
    Output: The prisoner number which has the word in his/her statement
    '''
    f=open(file)
    csv_reader=csv.reader(f)
    l=[] #Empty list
    for line in csv_reader:
        l.append(line)
    f.close()
    #Here we have list of lists
    d={} #Empty dictionary
    for eachlist in l: #Each offender has a line
        statement=removepunc(eachlist[8]) #This is the statement of each offender. And you want to apply removepunc
        for word in statement: #Each word in statement
            d.setdefault(word, []) #Create a dictionary with keys of the word and a empty list in those keys
            if eachlist[3] not in d[word]: #If the prisoner number is not in the word
                d[word].append(eachlist[3]) #Add the prisoner number to each word
                
    for w in d:
        if w==word:
            return d[w]

    
prisonernumbers=invertedindex("offenders-clean.csv")
#For some reason python only render offenders-clean not offenders

print(removepunc('I have an apple.'))
print('\n----------------------------------------------------------------\n')
print(inputword('dead'))
print('\n----------------------------------------------------------------\n')       
print(invertedindex1('offenders-clean.csv', 'happy'))