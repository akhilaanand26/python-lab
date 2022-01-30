string=str(input("Enter the string:"))
a=string[0]
char=string.replace("o","$")
a=a+char[1:]
print(a)