def long(a):
   max=len(a[0])
   temp=a[0]
   for i in a:
        if(len(i)>max):
            max=len(i)
            temp=i
   print("The word with longest length is:",temp,"and length is",max)
a=["strawberry","orange","apple"]
long(a)