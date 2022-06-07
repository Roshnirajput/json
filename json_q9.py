# import json

# a={"shopping_list":{"choco":15,"suite":30,"dory_milk":20,"milky_bor":25}}
# def shope (item,howmany):
#     dict={}
#     for i in a:
#         for j in a[i]:
#             result=int(a[i][j]-howmany)
#             if item ==j:
#                 if howmany>0:
#                     dict [j]=result
#                     print(dict)
                    
# item=input("enter") 
# howmany=int(input("enter")) 
# shop(item,howmany) 
 
# b=open("json_q9.json","w") 
# c=json.dump(a,b,indent=5) 
# b.close () 
  
dic={"shopping_list":{        
 
             "chaco":"15",
             "biscuits":"50",
             "diary_milk":"30",
             "ice_cream":"20",
            } } 
import json
s={}  

for i in dic:
    s=dic[i]
    user=input("kon sa item chahiye")
    for j in s:
        if j==user:
            if user in s:
                iteam=int(input("kitne item chahiye"))
                total=(int(s[j]))-iteam
            break
    s[user]=str(total)
print(s)
# y=open("myfile9.json","w")
# json.dump(s,y)
# y.close()