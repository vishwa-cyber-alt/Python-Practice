#Check Last Element is Odd or Even
def CheckLast(a):
    a.sort(reverse=True)
    if (a[0]%2==0):
        print("Last Element is ",a[0])
        print("even")
    else:
        print("Last Element is ",a[0])
        print("odd")
CheckLast([1,2,3,4,9])
CheckLast([1,2,3,4,6])
