'''
def freq(x,s):
  count=0
  for i in s:
    if i==x:
      count+=1
  return count,x

def routine_encode(s):
    list1=[]
    for ch in s:
        list1.append(freq(ch,s))
    for i in list1:
    #print(list1.count(i))
        if list1.count(i)>=1:
            list1.remove(i)
    if len(list1)>1:
        for i in list1:
            if list1.count(i)>1:
                list1.remove(i)
    return list1
print(routine_encode('ab'))
print(routine_encode('aaaa'))
print(routine_encode('aaaaa'))
'''
'''
Notes 10/23/17:
-for case 'abc', there only gets 1 b not 1 a and 1 c
'''
'''  
print(routine_encode('bbaaa'))
print(routine_encode('aaabb'))
print(routine_encode('abc'))
print(routine_encode('aa'))
print(routine_encode('aaaaa'))
print(routine_encode('aaaabbbbcccc'))
#should get 1,a,1,b,1,c
'''
'''
def routine_encode(s):
  list1=[]
  for ch in s:
    list1.append(freq(ch,s))
  for i in list1:
    #print(list1.count(i))
    if list1.count(i)>1:
        list1.remove(i)
    
  return list1
'''
'''
PROBLEMS:
-this works but once the items in the get longer than 3 than it returns double
-no idea how to fix
'''
#print(routine_encode('aaa'))
#print(routine_encode('aaaa'))
#print(routine_encode('aaaaa'))
'''
def routine_encode1(s):
    list1=[]
    for ch in (s):
        list1.append(s.count(ch))
        list1.append(ch)
    count=0
    for i in list1:
        if i
    return list1
    
print(routine_encode1('aa'))
'''
'''
def freq(x,s):
  count=0
  for i in s:
    if i==x:
      count+=1
  return count,x
  
def routine_encode(s):
  list1=[]
  for ch in s:
    list1.append(freq(ch,s))
  for i in list1:
    #print(list1.count(i))
    if list1.count(i)>1:
        del list1[list1.index(i)]
  return list1

print(routine_encode('a'))
print(routine_encode('ab'))
print(routine_encode('abc'))
print(routine_encode('aa'))
print(routine_encode('aaaaa'))
a=['a','b','a','c','a']
'''
'''
PROBLEMS:
RUNNING INTO THE SAME PROBLEM. 'aaaaa' gives me 5,a,5,a
'''
'''
def routine_encode2(s):
    list1=[]
    for count, ch in enumerate(s):
        print(count, s.count(ch), ch)
        #print(count,ch)
        
routine_encode2('aabc')
'''
'''
***THIS IS KAIZENS ANSWER***
-My problem with RLE was that I appended each ch and did not stop when two or more of the same characters appeared
-I did not know what to do

SOLUTION:
-Run a check that the next character is not the original first character
-Append the counts
-Refresh the counts
-Then you should be good
'''
'''
def routine_encode(s):
  list1=[] #start with an empty list
  curr = s[0] #curr starts with the first character
  counter = 0 #counter restarts
  for ch in s:
    print(ch)
    if ch != curr: #if the character changes .....
      if counter != 1: #"A single letter just gets encoded as is"
        list1.append(counter) #Counter before character
      list1.append(curr) #Record character to list
      curr = ch #change the current character
      counter = 0 #restart the counter
    counter+=1 #keep the counter up
    
  if counter != 1:
    list1.append(counter) #final record counter
    print(counter)
  list1.append(curr) #final record character
  print(curr)
    
  return list1
  
print(routine_encode('aab'))
'''
'''
THIS IS MY CODE I FINALLY GOT IT
'''
def routine_encode1(s):
    list1=[] #empty list for counts and letters
    curr=s[0] #first character that changes when the character is different
    count=0 #counter starts at 0, 
    for ch in s: #for every element in the string
        
        if ch!=curr: #If the next element does not equal to the current one
            list1.append(count)   #Add the count to list1
            if count==1: #if count is equal to 1
                list1.remove(count) #remove to the count that is 1
            list1.append(curr)    #Add the curr to list1
            curr=ch #Change the curr to the next significant letter
            count=0               #Reset the count
        count+=1 #add counter by 1
    
    #if count!=1:
     #   list1.append(count)
    list1.append(count) #if the if loops are all done. Add the count. Add the final count
    list1.append(curr) #Add the final curr.
    if count==1: #If the final count is equal to one
        list1.remove(count) #Remove the count from the list.
    
    return list1 #Return the list with the counts and characters

'''
    if ch==curr:     #If the current character is equal to the curr (the significant character) 
        list1.append(curr) #Add the curr to list1
'''
print(routine_encode1('a'))
print(routine_encode1('aaa'))
print(routine_encode1('aaaaaaaaaa'))
print(routine_encode1('aabccdeef'))
'''
Notes 10/25/17:
-CODE READS FROM TOP TO BOTTOM
-FOR LOOP FINISHES FIRST THEN IF LOOP
-IF THE COUNT EQUALS TO ONE IT IS REMOVED.
-I DID IT!!!!!!!!
'''
