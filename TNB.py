#it is find a two number betwween a numbers

Fn=int(input("Enter a no:"))
Ln=int(input("Enter a no:"))
Fn+=1
for i in range(Fn,Ln):
    print(i)
T=Ln-Fn
T-=1
print("Total number b/w in given no:",T)