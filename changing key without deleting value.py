#changing key without removing value
my_dict = {'name':'Peter Parker','Heroic_name':'spiderman','City':'New York'}

value_of_name = my_dict.pop('name')
my_dict['full name'] =value_of_name

print(my_dict)


#---------------------------------------------------------------------------------------
#without changing it place

dict1 = {'name Full':'Roger','Heroic_name':'Spiderman'}

dict1['name']  = dict1['name Full']

del dict1['name']
print(dict1)