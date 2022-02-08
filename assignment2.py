dic={}
a="saradha varam segregation pelnamyt"
for i in a:
    dic[i]=dic.get(i,0)+1
m=max(dic,key = dic.get)
print("lottery character is",m)
