s={'manu':42,'sam':32,'arya':12,'david':3}
y=list(s.items())
y.sort()
temp=dict(y)
print("Ascending order is",temp)
y.sort(reverse=True)
dict=dict(y)
print("Descending order is",dict)