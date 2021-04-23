import json
jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'
print(json.loads(jobj_dict))
print(json.loads(jobj_list))
print(json.loads(jobj_string))
print(json.loads(jobj_int))
print(json.loads(jobj_float))
#json encoded in python