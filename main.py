# --------------------Guessing game--------------
import random
import math

print('Welcome to my Guessing Game :) ') 

correct_guess = 'secrets'
Hint = '\n\v Tip: - What do people tend to keep from one-another in order to;\n Protect, Prevent self-percieved hardships, avoid strife or hide the truth.'
context = '\v It can be a plethora of things that people keep hidden to themselves..'
guess_count = 1
guess_count_limit = 5
guess = None

while guess != correct_guess:
   guess = input(f'{context}\n\v Guess the Word ! :  ')
   try:
        sGuess = str(guess)
   except:
         print ('Huhh! Did I not just say guess the WORD..')
         continue
   if sGuess != correct_guess and guess_count < guess_count_limit:
     print (f'\v Strike {guess_count} | Try again!', Hint)      
     guess_count = guess_count + 1
     continue
   elif guess_count == guess_count_limit:
     print ('\v B0ooM!!!, Limited Patience Reached..')
     print ('Pitiful..')
     quit()
   elif sGuess == correct_guess:
     break
print(f'\n Correct :)\n lucky guess!.. I guess?: {correct_guess}..indeed.')
