# functions 
def hello_world(): # define function
    print('Hello world')

hello_world() # call function

# function with argument
def arg_func(name, age):
    # print(str(name)+ ' ' + str(age)) # you can concatenate name & age
    # print('Saboor ' + str(28)) # or something like this
    # return (name +  " " + str(age)) # there could be more way to return or print a value
    if age < 18:
        print(f'Sorry {name} your age is {age}, you must be over 18 to get in')
    else:
        print(f'Welcome {name}, you age is {age}, and you are allowed')
arg_func('Saboor', 17)

# defining more functions 

def inner():
    animals = ['dog', 'car', 'horse', 'bear', '....']
    for x in sorted(animals):
           print( x, end=',' )
    # you can make any functionality here, and this function inside the outer function()
def outer():
    inner()
outer()
    