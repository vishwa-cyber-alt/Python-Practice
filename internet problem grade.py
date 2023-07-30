m=int(input("how many marks want to enter:"))
for i in range(0,m):
  ma.append(m)
print(ma)
m=int(input("how many marks want to enter:"))
for i in range(0,m):
  ma.append(m)
  for i in range(0,len(m)):
    if m[i]>80:
        g.apppend("Agrade")
    elif m[i]<80:
        g.append("fail")
  
print(ma)
