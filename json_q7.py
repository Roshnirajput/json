import json

d={"name":"abhishek","designation":"ceo of navgurkul","gender":"male",
   "age":29}
y=open("merafile43.json","w")
json.dump(d,y,indent=4)
y.close()