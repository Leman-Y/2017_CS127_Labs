def dictwords(wordlist):
    d={}
    for w in range(len(wordlist)-1):
        d.setdefault(wordlist[w],'')
        d[wordlist[w]]=''+str(wordlist[w+1])
    d.setdefault(wordlist[-1])
    
    return d
    
print(dictwords(['a','b','c','a','d']))