import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print(json.dumps(j_str,sort_keys=True , indent=4))

#2nd way
a=[]
b=[]
for key in j_str:
    a.append(key)
    b.append(j_str[key])
for i in range(0,len(a)):
    for j in range (0,len(b)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
            b[i],b[j]=b[j],b[i]
d={}
for index in range(0,len(a)):
    d[a[index]]=b[index]
with open("w3resourse4.json","w") as json_obj:
    data=json.dump(d,json_obj)
