import json
python_obj = {
     "name": "David",
     "class":"I",
     "age": 6  
 }
a=json.dumps(python_obj)
print(type(python_obj))
print(type(a))
#python to json