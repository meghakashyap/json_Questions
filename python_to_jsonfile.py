import json
a={1:"one",2:"two",3:"three"}
b=open("q.json","w")
json.dump(a,b,indent=4)
b.close()
#convert python into json file