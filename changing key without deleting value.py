#changing key without removing value
my_dict = {'name':'Peter Parker','Heroic_name':'spiderman','City':'New York'}

value_of_name = my_dict.pop('name')
my_dict['full name'] =value_of_name

print(my_dict)

