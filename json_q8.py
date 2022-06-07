import json
a=['neelam','programmer','20','20000']
b=['komal','trainer','24','24000']
c=['anuradha','hr','24','40000']
d=['abvishek','manager','29','63000']
e=[a,b,c,d]
list=["name","designation","age","salary"]
f=["emp1","emp2","emp3","emp4"]
g={}
i=0
while i<len(e):
    h={}
    j=0
    while j<len(e[i]):
        if j==0:
            h[list[j]]=e[i][j]
            # print(h)
        if j==1:
             h[list[j]]=e[i][j]
            #  print(h)
        if j==2:
            h[list[j]]=e[i][j]
            # print(h)
        if j==3:
             h[list[j]]=e[i[j]]
            #  print(h)
        i+=1
        g[f[i]]=h
    i+=1
# print(g)
with open("myfile8.json","w") as f:
    json.dump(g,f,indent=4)