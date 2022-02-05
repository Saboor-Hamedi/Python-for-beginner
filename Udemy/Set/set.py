# in this tutorial I will focus set 
# this is the opposite tuple and list, 
# a set would make through braces {}
from distutils.command.build_scripts import first_line_re
from re import I


my_first_set = {1,2,3,4,5}
# set items, Data types 
my_second_set = {'Ahmad' ,'Mahmmod', 'Rashid'}
my_third_set = {True, False}
print(my_first_set)
print(len(my_first_set))
print(my_second_set)
print(my_third_set)
# set with constract
set_const = set(('Hello', 'Hi', 'How are you?'))
print(set_const)
# loop through the set 
for x in set_const:
    # get the length of each set 
    get_len = len(x)
    print(x,',', get_len)
# check if set is exists 
if 'Hello' in set_const:
    print('Yes', 'the item is exists')
else:
    print('No the item is not exists')
# add new item
set_const.add('I am new item here, thank you for inviting.') # in set we use keyword add while in tuple and list we use append
print(set_const)
# we also can move item from set to another one
set_const.update(my_first_set)
print(set_const)
# add individual item 
set_individual =['Hey']
set_const.update(set_individual)
print(set_const)
# we can also remove item 
set_individual.remove('Hey')
print("I am empty now! ",set_individual)
# we can remove in two wasy an item, one by keyword of remove() another discard()
# if item do not exists remove will throw and exception
set_const.discard('I am new item here, thank you for inviting.')
print(set_const)
# remove last item
remove_last_item = set_const.pop();
print(remove_last_item)
# loop through the set
for x in my_second_set:
    print(x) 
# we can also join multiple sets 
s1 = set(['Book']) # also we can define set as this ([])
s2 = set(['Pencil'])
s3 = s1.union(s2) # you can also use update 
print(s1.update(s2))
print(s3)
# loop through 
for x in s3:
    print(x)
# to remove the entire set, use clear() 
clear_set = set_const.clear()
print(clear_set)
# we have del, which stands for delete, it well delete entire set 
# del my_first_set