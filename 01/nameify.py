#Write a program named nameify.py It should assign a string in the first line and the string will be in the form "word1 word2" where
#both words are lower case. The program should assign a new string where each of the two words are capitalized.
print('Write first word in lowercase letters')
word1=input()
print('Write second word in lowercase letters')
word2=input()
print(word1+' '+word2)
print(''+word1.upper()+' '+word2.upper()+'')