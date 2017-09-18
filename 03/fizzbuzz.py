
for x in range(1,101):
    if x%3==0 and x%5==0:
        msg=('fizzbuzz')
    elif x%3==0:
        msg=('fizz')
    elif x%5==0:
        msg=('buzz')
    else:
        msg=x
    print(msg)
        

'''
def multiples(n, count):
    for i in range(count):
        print(bizz)
'''
'''
copied this from internet for reference. my numbers were not getting replaced with the words so I would be getting multiples of 3,5 with the words.
if a then do that, elif b (if not then do b), else: (if not b then do this)
for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        msg = "FizzBuzz"
    elif num % 3 == 0:
        msg = "Fizz"
    elif num % 5 == 0:
        msg = "Buzz"
    else:
        msg = str(num)
    print (msg)
'''