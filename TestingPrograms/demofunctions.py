l1=[10,20,30]
l2=l1
print(l1)
l1.append(200)
print(l2)
print(id(l1))
print(id(l2))
l3=[43,23,12]
l4=l3.copy()
print(l3)
l3.append(13)
print(l4)
print(id(l3))
print(id(l4))
# function
def square(n):
    return n*n
print(square(10))

def getvalues(l):
    return sum(l),max(l)
num=[2,4,6,8,21]
s,m=getvalues(num)
print(s,m)
def fact(n):
   if(n==0):
       return 1
   else:
       return n*fact(n-1)

print(fact(4))
# reuse of a code
import demofunctions as df
print(df.fact(5))
def calculatewages(days,wages):
        print(days*wages)

calculatewages(5,500)
def demo(*n1):
    print(n1)
demo(10,20,30)
demo(10)
def demo2(**n1):
    print(n1)
demo2(name="ravi",num=100)