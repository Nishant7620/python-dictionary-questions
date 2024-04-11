my_dict = {'a': 1, 'b': 2, 'c': 3, 1:'Kakarot',2:'Goku'}

for item in my_dict:        #When we access dictionry it will only returns keys
    print(item)


#iterating through key
for key in my_dict:
    print(key,my_dict[key])    

#items method to iterate dictionary

for key,value in my_dict.items():
    print(f"Key {key}: Value {value}")
