#Joel Wilkins
#02/08
#Guessing game


import random
print('\n#### Welcome to the guessing game ####')
Name=input('Hello Player, what is your name? ')
print('\nHello', Name,'!')
upper=int(input('Please select your upper range: '))
number=random.randint(1,upper)
print(number)
print('You have six guesses!')
guesscount=0
guesslimit=6
while guesscount<guesslimit:
  guess=int(input('Please enter your guess: '))
  guesscount+=1
  if guess!=number and guesscount<guesslimit:
    print('Try again!')
  if guess==number:
    print('Correct')
    break
else:
  print('Unlucky!')
  
    
  
