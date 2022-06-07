import json
a={"name": "roshni", "class": "II", "age": 8}
b=open("json_q2.json","w")
json.dump(a,b,indent=2)
b.close()
