import sys 
x = sys.getrefcount(1)
print(x)

L = [1,2,3]
M = L
print(L==M)
print(M is L)
print(L is M)
name = str(input('Write your name: '))
counter = 0
age = 0
while True:
    counter += 1
    try:
        age = int(input(f'You have {counter} chances to enter a correct age, how old are you? ')) 
    except ValueError:
        if counter >=3: 
            break
        else:
            continue
    car = str(input('What is your car name? '))
    print(f'Name {name.capitalize()}, age is {age}, car name is {car.capitalize()}')
    break



        