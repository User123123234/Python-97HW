import random
number=int(random.randint(1,9))
guesses=0
while guesses<5:
    guesses=guesses+1
    guess=int(input('Enter a number: '))
    if (guess==number):
        print('You got it right!')
        print('YOU WIN!')
        break
    else:
        print('You got it wrong!')
if (guesses>=5):
    print('The number was '+str(number))
    print('YOU LOSE!')