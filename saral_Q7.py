import json
file_name="text_file.txt"
dict={}

with open(file_name) as file:
    for line in file:
        key,value=line.strip().split(None,1)
        dict[key]=value.strip()
out_file=open("q7.json","w")
json.dump(dict,out_file,indent=4)
out_file.close()
#convert text file data into json file data