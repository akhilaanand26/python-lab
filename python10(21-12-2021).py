a=input("Enter the word:")
def words(w):
    w1=w[-3:]
    if w1!="ing":
        print("adding 'ing'=",w+"ing")
    else:
        print("adding 'ly'=",w+"ly")
words(w=a)
