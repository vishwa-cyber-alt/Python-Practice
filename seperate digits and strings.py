a="welcome346pore9"
d=[]
s=[]
for i in a:
    if i.isdigit():
        d.append(i)
    else:
        s.append(i)
print(d)
print(s)
str=''.join(s)
dig=''.join(d)
print("strings=",str)
print("digits=", dig)

