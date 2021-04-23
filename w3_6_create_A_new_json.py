import json
with open("demo.json") as file:
    convert=json.load(file)

for  i in convert["abbreviation"]:
    del i ["abbreviation"]

with open("new.json","w") as file:
    json.dumps(convert, file,indent=3)

