#clear method()

my_dict = {'name':'Peter','age':25,'Heroic_name':'Spiderman'}

my_dict.clear()
print(my_dict)

#----------------------------------------------------------------------------------------------
#copy method()
#shallow copy()

original_dict = {'a':1,'b':[2,3],'c':{'x':4,'y':5}}

copied_dict = original_dict.copy()

original_dict['c'][0]=99
original_dict['a']=100

print(f'original Dictionary:{original_dict}')  #changes occurs in original dictionrry
print(f'copied dictionary:{copied_dict}')       #changes occurs only on list items

#---------------------------------------------------------------------------------------------------
#deep copy method
#import copy

import copy
original_dict = {'a':1,'b':[2,3],'c':{'x':4,'y':5}}

deep_copied_dict = copy.deepcopy(original_dict)

original_dict['b'][0] = 99
original_dict['a'] = 100

print(f'original Dictionary:{original_dict}')               #in deep copy changes only occurs in original data  
print(f'copied dictionary:{deep_copied_dict}')               #it will not affect in copied data   


#---------------------------------------------------------------------------------------
#fromkeys method()

keys =  ['a','b','b','d']

default_value = 100

new_dict = dict.fromkeys(keys,default_value)
print(new_dict)

#with mutiple values

keys = ['x','y','z']

default_value = (100,200)

new_dict = dict.fromkeys(keys,default_value)
print(new_dict)

#default value is not given

keys = ['x','y','z']

new_dict = dict.fromkeys(keys)
print(new_dict)



#------------------------------------------------------------------------------------------
#get method()

original_dict = {'a':1,'b':[2,3],'c':{'x':4,'y':5}}

print(original_dict.get('b'))
value_d = my_dict.get('d')   # Key 'd' is not present
print(original_dict.get('z',100))  # Key 'z' is not present with default value 100

#-----------------------------------------------------------------------------------------
#items method()

my_dict = {'a': 1, 'b': 2, 'c': 3}

items = my_dict.items()                             #using item to get key-value pair
print(items)


#accessing through loop


my_dict = {'a': 1, 'b': 2, 'c': 3}

for key,value in my_dict.items():
    print(f" key {key}: value {value}")


#----------------------------------------------------------------------------------------------
#keys method()

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(my_dict.keys())           #it will return keys present in dictionary

for key,value in my_dict.items():
    print(key)

#----------------------------------------------------------------------------------------------
#values method()
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

values = my_dict.values()
print(values)

#---------------------------------------------------------------------------------------------
#pop method()

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

pop = my_dict.pop('d')
print(pop)
print(my_dict)

#------------------------------------------------------------------------------------------
#pop items()
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

pop =my_dict.popitem()
print(pop)
print(my_dict)

#----------------------------------------------------------------------------------------
#set default()
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
value_a = my_dict.setdefault('a',100)
print(value_a)
print(my_dict)

value_e = my_dict.setdefault('e',200)
print(value_e)
print(my_dict)


#---------------------------------------------------------------------------------------------
#update method()

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

dict1.update(dict2)

print(dict1)
