s="madam"
s = ''.join(e for e in s if e.isalnum()).lower()
r=s[::-1]
if r==s:
    print("palindrome")
else:
    print("no")
