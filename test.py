dic=dict()
dic['a']=50
dic['dd']=73
dic[15]='fuck'
dic[66]=69
dic['fuck']='you'
dic['you']=2
print(dic)
list=list(dic)
print(list)
lk=dic.keys()
print(lk)
lv=dic.values()
print(lv)
print(lv[2])
li=dic.items()
print(li)

for k,v in li:
    print(k,v)
