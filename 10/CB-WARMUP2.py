'''
front_times
http://codingbat.com/prob/p165097
'''
def front_times(str, n):
  return str[0:3]*int(n)

#print(front_times('A', 4))

'''
last2
http://codingbat.com/prob/p145834
'''
'''
def last2(str):
  if len(str)<=2:
    return 0
  if len(str)>=3:
    q=str[-2]+str[-1]
    b=str.count(q)
    return b-1

      
print(last2('1717171'))
'''
def last2(str):
  if len(str)<=2: #less than or equal to two there is no last2 that would count 1
    return 0
  if len(str)>=3: #if length of string is greater or equal than 3
    q=str[-2]+str[-1] #last two characters
    count=0 #start at 0
    for i in range(len(str)-1):
      if str[i]+str[i+1]==q: #if str[i:i+2]==q 
        count+=1  #add 1 to the count
    return count-1 #minus 1, because you don't count end substring

#print(last2('axxxaaxx'))

'''
array123
http://codingbat.com/prob/p193604
mainthing.count(thingyouwannacount) takes into considerationt the order
'''
def array123(nums):
  if len(nums)<3:
    return False
  if nums==[1,2,3]:
    return True
  emptystring=''
  for i in nums:
    emptystring+=str(i)
    a='123'
    if emptystring.count(a)>=1:
      return True
  else: 
    return False

#print(array123([1, 1, 2, 3, 1]))

'''
string_bits
http://codingbat.com/prob/p113152
'''
def string_bits(str):
  emptystring=''#empty string add letters into
  for i in range(len(str)): #the numbers in the range of str
    if i%2==0:  #if the number i is divisible by 2 and gets zero
      emptystring+=str[i]  #add the character at the index i to the emptystring
  return emptystring

#print(string_bits('HiHiHi'))

'''
array_count9
http://codingbat.com/prob/p166170
'''
def array_count9(nums):
  count=0
  for i in range(len(nums)):
    if nums[i]==9:
      count+=1
  return count
      
#print(array_count9([1, 9, 9]))

'''
string_match
http://codingbat.com/prob/p182414
NOTES 11/1/17:
-WHATS THE DIFFERENCE?
-WHAT AM I DOING WRONG BETWEEN STRING_MATCH VS STRING_MATCH1
'''
def string_match(a, b):
    count=0
    if len(a)>=2 and len(b)>=2:
        for i in range(len(a)-1):
            for x in range(len(b)-1):
                if a[i]==b[x]:
                    if a[i+1]==b[x+1]:
                        count+=1
    return count

print(string_match('aabbccdd', 'abbbxxd'))

def string_match1(a,b):
    count=0 #count the same length 2 substring
    for i in range(len(a)-1): #Loop i over every character
        q=a[i:i+2]  #character and the next character at position i
        w=b[i:i+2]
        if q==w: #if the substring equals each other
            count+=1 #Add to count
    return count

print(string_match1('aabbccdd', 'abbbxxd'))

'''
Notes:

'''