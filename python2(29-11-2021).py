list=[]
n=int(input("Enter the limit:"))
print("Enter the elements:")
for i in range(n):
    element=int(input())
    if(element>100):
        list.append("over")
    else:
        list.append(element)
print(list)