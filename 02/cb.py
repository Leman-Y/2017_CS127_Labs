'''
*STRING_TIMES*
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def string_times(str, n):
    return(str*n)
    
print(string_times('hi',3))

'''
*FRONT_TIMES*
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or
whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def front_times(str, n):
    front_len=str[:3]
    return (front_len*n)

print(front_times('Abc', 3))

'''
#not my code, i copied
*String_Bits*

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''
#range() only works for integers and it works alongside len() which tells you the characters
def string_bits(str):
  result = ""
  for x in range(len(str)):
    if x % 2 == 0:
      result+=str[x]
  return result
print(string_bits('Heeololeo'))

'''
How do I just pick all the even characters and put them together to form a new string?
'''

'''
LONE_SUM
'''
def lone_sum(a, b, c):
  if a==b and b==c and c==a:
    return 0
  if a==b:
    return c
  if b==c:
    return a
  if a==c:
    return b
  return a+b+c
print(lone_sum(9,3,5))
#Why cant I say if a==b==c is false: then return a+b+c?
#a!=b!=c does not work as well

'''
#not my code, i copied
STRING_SPLOSION
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''
def string_splosion(str):
    result = ''
    for i in range(len(str)+1):
        result += str[:i]
    return result
print(string_splosion('Code'))
'''
Cigar_Party
'''
def cigar_party(cigars, is_weekend):
  x=cigars
  if 40<=x<=60:
    return True
  if is_weekend:
    if x>=60:
      return True
    if x<=40:
      return False
  else:
    return False

print(cigar_party(30, True))

'''
CAUGHT_SPEEDING
'''

def caught_speeding(speed, is_birthday):
  x=speed
  if is_birthday:
    x-=5
  if x<=60:
    return 0
  if 61<=x<=80:
    return 1
  if x>=81:
    return 2

print(caught_speeding(65, False))





    
