n1= int(input("Enter the limit"))
n2=int(input("Enter the last limit:"))
for number in range(n1,n2+1):
    if number>1:
        i=2
        for i  in range(2,number):
            if(number%2==0):
                break
        else:
            print(number)