n1=0
n2=1
num=int(input("Enter the limit"))
print(n1)
print(n2)
for num in range(0,num-1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
