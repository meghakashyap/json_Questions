#Python object ko json string mai convert karne ka program likho?
import json
python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)

print("python_dictionary =",json.dumps(python_dict))
print("python_list =",json.dumps(python_list))
print("python_string =",json.dumps(python_str))
print("python_intiger =",json.dumps(python_int))
print("python_float =",json.dumps(python_float))
print("python_Ture =",json.dumps(python_T))
print("python_False =",json.dumps(python_F))
print("python_Null =",json.dumps(python_N))