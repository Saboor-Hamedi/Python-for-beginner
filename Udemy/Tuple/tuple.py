#tuple, in this tutorial we have a look to the tuple, I will try to cover them all 
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# A tuple is a collection which is ordered and unchangeable, unlike the list

my_tuple = ('Dog', 'Cat', 'horse')
print(my_tuple)
# show data type
print(type(my_tuple))
# get the len of the tuple 
print(len(my_tuple))
# create item with one item
# a tupel can have duplicate data 
duplicate_tuple = ('Dog', 'Cat', 'horse', 'horse')
print(duplicate_tuple)
# tuple  construct 
cons_tuple = tuple(('Hello', 'Hi', "I'm saboor"))
print(cons_tuple)
# access each item through its index number 
print(cons_tuple[1])
print(cons_tuple[-1]) # print the last item, this is the same as list 
# check it item exists 
if 'Hello' in cons_tuple:
    print('Yes,', 'that is there')
else:
    print('The item did not match')
# change the item, you will get nothing
#------------------------
#change the tuple, 
#first convert tuple into list, then change it to tuple back
convert_tuple = list(cons_tuple)
convert_tuple[0] = 'You update me, thank you'
tuple_update = tuple(convert_tuple)
#you can add item too
print(tuple_update)
# same process for adding new item
add_new_item = list(cons_tuple)
add_new_item.append('Im new here')
cons_tuple = tuple(add_new_item)
print(cons_tuple)
# loop tuple 
for x in cons_tuple:
    # you can get the lens also 
    get_len = len(x)
    print(x,', ', get_len)