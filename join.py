a="WelcomeToIndia"
lower=[]
up=[]
for i in a:
    if i.islower():
        lower.append(i)
        
    else:
        up.append(i)
f=''.join(lower+up)
print(f)
        
print(lower)
print(up)
