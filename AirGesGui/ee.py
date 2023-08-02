a=input().lower().replace(' ','')
print('pangram') if len(set(a))==26 else print('not pangram')
