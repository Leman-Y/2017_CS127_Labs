'''
*THIS IS KAIZENS CODE. HE HELPED ME OUT.*

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

        