'''
1. write a routine rle_decode which will decode a list that represents the rle encoding you did on the test.
    So, the list [2,'a', 3, 'b', 'c', 2,'d']  should return "aabbbcdd"

You'll have to determine if an element is an int or a char so you'll have to look that up.
'''
'''
def rle_decode(s):
    string=''#empty string
    
    for element in s: #For every item in s(list) 
        string+=str(element) #Turn the element into a string and add it into an empty list
        #Now I am able to use isdigit() and isalpha()
    
    print(string)
    ch=0 #ch is zero
    ch1=0 #ch1 is zero
    string1='' #Final string answer

    for char in string:

        if char.isdigit() is True: #If char is a number
            a=string.index(char) #Get the position of the number in the string
            string1+=int(char)*string[a+1] #Number times the next letter. 2,a will become aa
            
        if char.isalpha() is True:
            b=string.index(char) 
            #print(b)
            if string[b-1].isdigit() is False:
               string1+=char
    
    return string1

print(rle_decode([2,'c', 2,'d']))
#print(rle_decode(['z',1,'a','c',3,'b','e']))
#print(rle_decode([2,'a', 3, 'b', 'c', 2,'d']))
'''
'''
        
    
    #for element in s:
        #if element.isdigit() is True:
          #  print(element)
        #if element.isalpha() is True:
        #    print(element)

print(rle_decode([1,'a','d',3,'b','c']))

'''
'''
Notes 10/29/17:
-If there is no integer before the letter. Then just print that letter.
-If there is an integer. Integer times the letter
-Append these to the list
-Determine if character is a number or letter
-Make a list and append to that list

'''
'''
a=[2,'a', 3, 'b', 'c', 2,'d']
c=''
for i in a:
    c+=str(i)
    
print(c)
'''

def rle_decode1(s):
    string=''#empty string
    
    for element in s: #For every item in s(list) 
        string+=str(element) #Turn the element into a string and add it into an empty list
        #Now I am able to use isdigit() and isalpha()
    
    string1=''
    
    for count, char in enumerate(string):
        if char.isdigit() is True:
            #print(string[count+1])
            string1+=int(char)*str(string[count+1])
        
        if char.isalpha() is True:
            if string[count-1].isdigit() is False:
                string1+=char 
            
    return string1
            
            
print(rle_decode1(['a']))
print(rle_decode1([2,'c', 2,'d']))
print(rle_decode1([2,'a', 3, 'b', 'c', 2,'d']))

'''
Notes FIX:
-When I inputed [2,'c', 2,'d'] in my first rle_decode, It would give me cccc not ccddd, because the char+1 in the position would revert
-back to the first 2.
-I made a count to distinguish the first 2 and all the others 2s.
-This would allow me to properly determine which position I want the character to be in.
'''
