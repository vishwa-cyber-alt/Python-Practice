def generator():
    yield 1
    yield "hello"
    yield 9
    yield 12
for i in generator():
    print(i)
