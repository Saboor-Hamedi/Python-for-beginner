# finve average, count total of number, and display the odd number
numbers = [5,10,25,52,19,212,938,100]
event = []
average_number = sum(numbers)
length = len(numbers)
average = average_number/length
print(f'Average number is: {int(average)}', f'- count: {length}')
for  number in numbers:
    if number % 2 == 0:
        event.append(number)
print(event)



    