import random

secret_number = random.randint(1, 101)
user_guesses = [];
number_found = False
while not number_found:
    guess = int(input("Enter your guess (1 to 100) : "))
    user_guesses.append(guess)
    if guess == secret_number:
        print("You Won!!\n"
              "Your tries ", set(user_guesses))
        number_found = True;
    elif guess < secret_number:
        print("you guess too small")
    else:
        print("your guess too large")
