class Cal:
    a=int(input("Enter no a:"))
    b=int(input("Enter no b:"))
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def rem(a,b):
        return a//b
    
    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))
    print(div(a,b))
    print(rem(a,b))



class Fun:
    def fun(a):
        print("Enter a no:",a)
    print(fun(5))