def function(text):
    def function1():
        print(text)
    return text
print(function("hello"))
def add_num(n):
    def add(x):
        return x+n
    return add
num1=add_num(10)
num2=add_num(12)
print(num1(5))
print(num2(6))
def function1(func):
    def function2():
        print("hello function2")
        func()
    return function2
def demo():
    print("hello demo")
f=function1(demo)
f()