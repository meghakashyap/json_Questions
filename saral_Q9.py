import json
dict={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
add=input("If you want to add something in shopping list press Y or N for no=")
item=input("enter which item would you like to buy=")
no_of_item=int(input("PLEASE enter How many item would you like to buy ="))
for key in dict:
    for value in dict[key]:
        if value == item:
            dict[key][value]=int(dict[key][value])-no_of_item
    if "y"  == add:
        dict[key][item]=str(no_of_item)
print(json.dumps(dict, indent=4))
#python to json(shopping list)  
  

        