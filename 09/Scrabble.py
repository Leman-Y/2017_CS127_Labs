def score(w):
  sum1=0
  for ch in w:
    if ch.lower() in 'aeioulnrst':
      sum1+=1
    if ch.lower() in 'dg':
      sum1+=2
    if ch.lower() in 'bcmp':
      sum1+=3
    if ch.lower() in 'fhvwy':
      sum1+=4
    if ch.lower() in 'k':
      sum1+=5
    if ch.lower() in 'jx':
      sum1+=8
    if ch.lower() in 'qz':
      sum1+=10
  return sum1
  
print(score('hello'))
print(score('THIS IS A WORD...'))
print(score('q ,j,k,23'))
print(score('a'))
print(score('d'))
print(score('b'))
print(score('F'))
print(score('k'))
print(score('j'))
print(score('q'))
