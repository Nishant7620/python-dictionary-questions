dictionary = {}

#get number of key-value users wants to input

num = int(input("enter the number of entries"))

for _ in range(num):
    key = input("enter a key: ")
    value = input("enter a value: ")

    dictionary.update({key:value})

print(F"user Dictionary: {dictionary}")