
#How do you check if a key exists in a Python dictionary

my_dict = {'a':1,'b':2,'c':3,'d':4}

print(my_dict.get('d',0))

#How can you retrieve all keys from a dictionary
my_dict = {'a':1,'b':2,'c':3,'d':4}
print(my_dict.keys())
for key in my_dict:
    print(key)


#How do you add a new key-value pair to an existing dictionary    
my_dict = {'a':1,'b':2,'c':3,'d':4}

my_dict.update({'e':5})
print(my_dict)

#How can you remove a key-value pair from a dictionary
my_dict = {'a':1,'b':2,'c':3,'d':4}

my_dict.pop('d')
print(my_dict)

#How do you iterate over key-value pairs in a dictionary
my_dict = {'a':1,'b':2,'c':3,'d':4}

for key,value in my_dict.items():
    print(f"{key}:{value}")


#How can you merge two dictionaries in Python

dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5}

dict1.update(dict2)
print(dict1)

#Given a dictionary my_dict, write a Python function to remove 
# all key-value pairs where the value is less than 10.
my_dict = {'a':1,'b':2,'c':12,'d':11}

keys_to_remove = []

for key,value in my_dict.items():
    if value<10:
        keys_to_remove.append(key)

# for key in keys_to_remove:
#     del my_dict[key]

# print(my)




