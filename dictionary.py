# empty dictionary

dict1 = {}
print(dict1)

#-------------------------------------------------------------------------------------------------
#dictionary syntax 

dict2 = {'name':"Nishant","age":21,"location":"Navi-Mumbai"}

print(dict2)

#-------------------------------------------------------------------------------------------------
#Dictionary Key

my_dict = {"name":"Roger","Heroic_name":"Captaion America","power":"shield"}

numeric_dict = {1:"one",2:"two",3:"three",}

tuple_dict = {('a',1):"value1",('b',2):"value2"}

print(my_dict)
print(numeric_dict)
print(tuple_dict)

#-----------------------------------------------------------------------------------------------------
#Dictionary Values

string_values = {'name':'John','age':25,'city':"New York"}

list_values = {'numbers':[1,2,3],'colors':['red','green','yellow']}

print(string_values)
print(list_values)

string_values['name']='Peter'
print(string_values)

#------------------------------------------------------------------------------------------------------
# accessing Dictionary values
string_values = {'name':'John','age':25,'city':"New York",1:1}

print(string_values['name'])
print(string_values['age'])
print(string_values['city'])
print(string_values[1])

