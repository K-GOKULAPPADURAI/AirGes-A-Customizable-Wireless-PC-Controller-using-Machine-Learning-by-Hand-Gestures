file=open('setgu.txt','r')
l=[]
for i in file:
    l.append(i.lower().rstrip('\n'))
ll=[]
for i in l:
    ll.append(i.split(','))
sck=[]
for i in ll:
    sck.append(i[1].split('+'))
            #print(sck
a=list(zip(ll[0],sck))
print(a)
file.close()
