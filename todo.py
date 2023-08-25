t=[]
while True:
    n=int(input("value="))
    if n==1:
      a=input("tasks:")
      t.append(a)
    elif n==2:
        print(t)
    elif n==3:
        b=input("remove=")
        t.remove(b)
        print(t)
