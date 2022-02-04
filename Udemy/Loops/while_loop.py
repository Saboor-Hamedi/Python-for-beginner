# while loop
import math
import random as rn
import  math as mat
x_number = 1
while x_number < 6:
    print(x_number)
    if x_number == 3:
        break
    x_number += 1  #  stop the loop one its over
print('-----------Enter you number---------------')
table_active = True

# Set up while loop
while table_active:
    lower = int(input("Enter lower bound\t"))
    upper = int(input("Enter upper bound\t"))
    number = rn.randint(lower, upper)
    print(" You have only have, ", round(math.log(upper - lower + 1, 2)), "chances to guess the number\t")
    count = 0
    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Guess a number\t"))
        #  condition testing
        if number == guess:
            print("You won\t")
            break
        elif number > guess:
            print("Your guess is too small\t")
        elif number < guess:
            print("Your guess is too high\t")

    # if guess is morethen the required guess
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d: "%number)








