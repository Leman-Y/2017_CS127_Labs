
def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1
    
print('Input any number')
x=input()
while x!=1:
    x=collatz(int(x))
    
    
