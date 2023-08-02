file=open('setgu.txt','r')
l=[]
for i in file:
    l.append(i.lower().rstrip('\n'))
ll=[]
for i in l:
    ll.append(i.split(','))
sck=[]
print(ll)
for i in ll:
    sck.append(i[1].split('+'))
                            #print(sck
          #print(a)
file.close()
dictt={'1':'','2':'','3':'','4':'','0':''}
dictt.update(dict(ll))
print(dictt)
