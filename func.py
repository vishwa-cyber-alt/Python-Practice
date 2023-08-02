def Check_Anagram(s,t):
    a=sorted(s)
    b=sorted(t)
    if a==b:
       print("yes")
    else:
        print("no")
Check_Anagram("rat","car")
Check_Anagram("vishwa","ivhsaw")
