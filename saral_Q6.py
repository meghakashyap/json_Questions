import json
json_obj='{"a":1,"a":  2,"a":  3, "a": 4, "b": 1, "b": 2}'
dict_ob=json.loads(json_obj)
print(dict_ob)
#find unique key