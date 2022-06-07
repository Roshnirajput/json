import json

a={'4':5,
   '6':7,
   '1':3,
   '2':4
}
   
b=dict(sorted(a.items()))
c = open('json_q4.json','w')
json.dump(b,c,indent=4)
c.close()
