'''
CODING BAT WARMUP-1
'''

'''
monkey_trouble 
#http://codingbat.com/prob/p120546
'''

def monkey_trouble(a_smile, b_smile):
  if a_smile==True and b_smile==True:  #Both true return True
    return True
  if a_smile==False and b_smile==False: #Both false return True
    return True
  else: #Other instances
    return False
'''
Notes:
return must be written as 'return' not 'Return'.
'''

'''
parrot_trouble 
#http://codingbat.com/prob/p166884
'''

def parrot_trouble(talking, hour):
  
  if talking==True and hour<7: #If bird is talking and is before 7, return True
    return True
    
  if talking==True and 7<=hour<=20: #If bird is talking and is between the parameters return False
    return False
    
  if talking==True and hour>20: #If bird is talking and is after 20, return True 
    return True
    
  else: 
    return False #I did the test cases, so everything else is False
  #You not in trouble if bird is talking regardless of what time it is
    
'''
pos_neg
#http://codingbat.com/prob/p162058
'''

def pos_neg(a, b, negative):
  if a<0 and b<0:        #3 Values that are depend on each other
    if negative==True:
      return True
    if negative==False:
      return False
  if a<0 and b>0:
    if negative==True:
      return False
    else:
      return True
  if a>0 and b<0:
    if negative==True:
      return False
    else:
      return True
  else: 
    return False

'''
front_back
http://codingbat.com/prob/p153599
-Both solutions work but codingbat wouldn't allow it
'''
def front_back(str):
  if len(str)<=1:
    return str
  if len(str)==2:
    return str[-1]+str[0]
  if len(str)==3:
    return str[-1]+str[1]+str[0]
  else:
    return str[-1]+str[1:-1]+str[0]

#print(front_back(''))
#print(front_back('a'))
#print(front_back('ab'))
#print(front_back('abc'))
#print(front_back('abcd'))

def front_back(str):
  if len(str)==0:
    return str
  if len(str)==1:
    return str
  if len(str)==2:
    return str[-1]+str[0]
  if len(str)==3:
    return str[-1]+str[1]+str[0]
  else:
    return str[-1]+str[1:-1]+str[0]

'''
sum_double
http://codingbat.com/prob/p141905
Notes:
-Python does not understand 2(a), but understands 2*a
'''

def sum_double(a, b):
  if int(a)!=int(b):
    return int(a)+int(b)
  else:
    return (a+b)*2

'''
makes10
http://codingbat.com/prob/p124984
Notes:
-You have to do a==10 and b==10. Not just a or b==10. You have to set the condition for both.
'''

def makes10(a, b):
  if a==10 or b==10:
    return True
  if a+b==10:
    return True
  else:
    return False


print(makes10(9, 9))

'''
not_string
http://codingbat.com/prob/p189441
'''

def not_string(str):
  if len(str)<3: #If len is less than three then it doesn't have not in it
    return ('not'+' '+str)
  if str=='not': #If string equals not then just return not
    return str
  if str[0:3]=='not':
    return str
  else:
    return 'not'+' '+str

'''
front3
http://codingbat.com/prob/p147920
'''

def front3(str):
  if len(str)<3:
    return str*3
  if len(str)>=3:
    return str[0:3]*3
