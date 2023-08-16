s = "a b c d e f a a b c a gd w a"
a = s.split()  
c = 0
for i in a:
    if i == "a":
        c += 1
print(c)
