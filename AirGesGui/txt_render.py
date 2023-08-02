file=open('Chrome.txt','r')
l=[]
for i in file:
    l.append(i.lower().rstrip('\n'))
file.close()
ll=[]
for i in l:
    ll.append(i.split(','))
print(['fin_count','sht_key','Desc'])
for i in ll:
    print(i)
    
sck=[]
for i in ll:
    sck.append(i[1].split('+'))
#print(sck)
lll=[]
for i in ll:
    lll.append([i[0],i[-1]])
#print(lll)


