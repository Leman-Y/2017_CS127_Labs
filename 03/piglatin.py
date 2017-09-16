
def piglatin(s):
    first_letter=s[0]
    if first_letter in 'aeiou':
        return (s+'ay')
    else:
        return (s[1:]+s[0]+'ay')
        
print(piglatin('apple'))
print(piglatin('latin'))
'''
print('__________________________________________')
s=str('apple')
print(s)
print(s[0])
first=s[1]
print(first)
'''