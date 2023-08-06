a=input()
b=input()
v='aeiou'
if any(char in v for char in a):
    print(b[::-1])
else:
    print(b)
    print("no vowels")
