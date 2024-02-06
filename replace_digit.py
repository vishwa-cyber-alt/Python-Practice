//replace digit 
a="a1b2c3d4"
r="d"
for i in a:
    if i.isdigit():
        a=a.replace(i,r)
print(a)
