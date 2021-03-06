# List tutorial
from os import remove
from re import L
my_list = [3,4,5,6,7,8,9]
my_list2 = ['Hello world', 23, True, 23.3]
my_list3 = ['How are you?', True, my_list2]
print(my_list)
print(my_list2)
print(my_list3)
# functions
my_range = list(range(15)) # generate a list of 15 numbers
# Using the brackets [] to make list
w = ['a', 'b', 'c', 'e']
print(type(w))
print(w[0])
print(w)
print(w[1])
print(w[0:1])
print(w[1:3])
print(w[-1])
# overwrite value 
print(w)
w[1] = 'saboor'
print(w)
# new list 
new_list = list(['mike', 'john', 'tom', 'smit', 'nouha', 'megelo'])
print(new_list)
print(new_list[:3])
print(new_list[3:])
print(new_list[3:-1])
# check if item is exists
if 'mike' in new_list:
    print("""Yes, Item is exists, 
             do you want to remove it?""")

# insert new item
new_list.insert(2, 'Hello world')
print(new_list)
#add new item
new_list.append('This is a espicial name')
print(new_list)
# merge ro expend two lists 
w.extend(new_list)
print(w)
for x in w:
    show_list = len(x)
    print(x, show_list)
# remove list 
new_list.remove('Hello world')
print(new_list)
#POP removes a specific index [1]
remove_item =[1,2,3,4]
remove_item.pop(1)
print(remove_item)
# if do not especify, will remove the last item
remove_item.pop()
print(remove_item)
# loop list 
loop_list = ['mike', 'john', 'tom', 'smit', 'nouha', 'megelo']
print(loop_list)
for x in loop_list:
    print(x, end=',')
# loop through the index number 
for i in range(len(loop_list)):
    print(i)
# join lists 
list1 = ['Book', 'Pencil', 'Pen']
list2 = ['Pencil case', 'Book cover', 'Book Page number']
print(list1)
print(list2)
print('After joining lists')
for x in list2:
    list1.append(x)
print(list1)
# count item
count_item = list1.count('Pencil') # item must be in the list, also it should not be nore then 1 item
print(count_item)

# this is a comment
"""
In general, the built-in slice() creates a slice object that can be used anywhere a slice
is allowed
"""
my_slice = [1,2,3,4,5,6,7]
a = slice(2,4)
print(my_slice[a])
# get more info about slice 
print(a.start)
print(a.step)
print(a.stop)
# map slice 
s= 'HelloSaboor'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])
del my_slice[a]
print(my_slice[a], 'has deleted')
