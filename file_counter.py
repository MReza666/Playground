while True:
    fname=input("Inseert File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        print("The file could not be found, please try again")
#
counter=dict()
for line in fhandle:
    wordlist=line.split()
    for word in wordlist:
        counter[word]=counter.get(word,0)+1
#
bigword=None
bigcount=None
for word,count in counter.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
#
print("Max frequent word is '",bigword,"' with ",bigcount," repeat")
