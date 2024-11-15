import random
secret_number = random.randint(1, 99)
print('Guess the number from 1 to 99.')

for guess_taken in range(1, 9):
    print('Input a number.')
    guess = int(input())

    if guess < secret_number:
        print('It is smaller.')
    elif guess > secret_number:
        print('It is larger.')
    else:
        break

if guess == secret_number:
    print('Right! You got it in ' + str(guess_taken) + ' times!')
else:
    print('Unlucky. The correct answer is ' + str(secret_number) + '.')