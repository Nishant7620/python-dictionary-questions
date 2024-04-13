
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

for key in keys_to_remove:
    del my_dict[key]

print(my_dict)


#Write a Python function that takes a list of words as input and returns a dictionary 
# where the keys are the unique words and the values are the frequencies of those words in the list.

# list1= []

# length = int(input('enter a length of dictionary'))
# for item in range(length):
#     user_input = (input("Enter a word"))
#     list1.append(user_input)

# new_dict = {}
# for word in list1:
#     new_dict[word]=len(word)
# print(new_dict)

# def word_frequency(words):
#     frequency_dict = {}
#     for word in words:
#         if word in frequency_dict:
#             frequency_dict[word] += 1
#         else:
#             frequency_dict[word] = 1
#     return frequency_dict

# list1 = []
# length = int(input("Enter the number of words: "))
# for i in range(length):
#     word = input("Enter a word: ")
#     list1.append(word)

# result_dict = word_frequency(list1)
# print(result_dict)


#Given a nested dictionary my_dict, write a Python function to access a 
# specific value by providing the keys as arguments. For example, if my_dict = {'a': {'b': {'c': 5}}},
# calling get_nested_value(my_dict, 'a', 'b', 'c') should return 5

my_dict = {'a': {'b': {'c': 5}}}

# def get_nested_value(value):
#     return(my_dict['a']['b']['c'])
# print(get_nested_value(my_dict))    

def get_nested_value(dictionary,*keys):
    nested_value = dictionary
    for key in keys:
        nested_value = nested_value[key]
    return nested_value
print(get_nested_value(my_dict,'a','b','c'))        

#Write a Python function to find the intersection of two dictionaries. 
# The intersection of dictionaries dict1 and dict2 is a dictionary
#  containing only the key-value pairs that are common to both dictionaries.