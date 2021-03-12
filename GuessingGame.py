secret_number = 7
guess_count = 0
guess_limit = 5
while guess_count < guess_limit :
    guess = int(input("Guess the number, you have 5 chances: "))
    guess_count += 1
    if guess == secret_number:
        print("You won! Congratulations")
        break
else:
    print("Sorry, wrong guess.")
