l=[i for i in range(40)]
p=iter(l)
# print(next(p))-->o/p:0
# print(next(p))-->o/p:1
for x in p:
    print(x)
def num():
    m=1
    print("First")
    yield m
    m+=2
    print("Second")
    yield m
    m+=2
    print("third")
    yield m
x=num()
# print(next(x))
# print(next(x))
for p in num():
    print(p)

import time
l=[i for i in range(1000)]
p=iter(l)
start_time=time.time()
for x in p:
    print(x)
end_time=time.time()
print((end_time-start_time)*10**3)
def geteven(l):
    for i in l:
        if(i%2==0):
            yield i
l=[i for i in range(100)]
x=geteven(l)
for i in x:
    print(i)
def gete(p):
    for i in p:
        if i%2==0:
            yield i
def geto(p):
    for i in p:
        if i%2!=0:
            yield i
def ope(fun,p):
    r=fun(p)
    return r
p=[i for i in range(100)]
x=ope(gete,p)
x=ope(geto,p)
for i in x:
    print(i)