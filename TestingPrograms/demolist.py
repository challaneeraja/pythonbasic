num = [10, 20, 30, 40]
print(num[1])
num.append(50)
print(num)
num.insert(2, 100)
print(num)
num.insert(10, 200)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num[2] = 250
print(num[2])
num.remove(40)
print(num)
print(num)
data=[]
data=reverseed(num)
print(list(data))
print(num)
# slicing
std = [10, 20, 30, 40, 50, 60]
print(std[1:4])
print(std[-1:-4:-1])
print(std[::2])
print(std[-5])
print(sum(num))
print(max(num))
print(min(num))
std=[[10,20,30],[45,50,65]]
print(std[0:1])
print(std[0][0:2])
print(max(std[0]))
print(sum(std[0]))
print(min(std[1]))
for n in std:
    for m in std:
        print(n[m])
        print(sum(n))
        print(max(n))
        print(min(n))
number=[1,2,4,5,6,7,9]
num1=len(number)
print(num1)
for num in range(num1):
    if((num1)%2==0):
        print(num*num)