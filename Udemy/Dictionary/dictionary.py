# in this tutorial I will cover dictionary
from hashlib import new


my_dic = {
    'Car': 'Toyota', 
    'Model': 2001, # Duplicates are not allowed 
    'Year': 2021, 
    'Color': 'White',
    'Colors': ['Yellow', 'Blue', 'Dark Gray'] 
}
print(type(my_dic))
# Dictionaries are used to store data values in key:value pairs.
print(my_dic) # print all values and keys 
print(my_dic['Car']) # get the value
dic_len = len(my_dic) # get the length of dic, 
print(dic_len) # display the len
# loop through the dictionary 
for x in my_dic:
    length = len(x) # get the length
    print(x,',', length)


# access items
x = my_dic['Car'] # this is the first way
print(x)
y = my_dic.get('Colors') # this is another way to fetch data
print(y)
for x in my_dic.get('Colors'): # extract data from []
    print(x)
# find all keys 
keys = my_dic.keys()
print(keys)
# get values 
dic_values = my_dic.values()
print(dic_values)
# get item 
dic_item = my_dic.items()
print(dic_item)
# we also add new item 
new_data = my_dic['Colors'] = 'Orange'
print(new_data)

# change item 
change_item = my_dic['Model'] = 2022
print(change_item)
#update dic 
update_dic = my_dic.update({'Car': 'Horse'})
