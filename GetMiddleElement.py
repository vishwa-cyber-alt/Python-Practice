def GetMiddleElement(n):
    convert=str(n)
    if len(convert)%2==0:
        print(n,"="," No Middle element")
    else:
        a=len(convert)//2
        print(n,"= ",convert[a])
GetMiddleElement(12345)
GetMiddleElement(123456)
GetMiddleElement(1234567)
