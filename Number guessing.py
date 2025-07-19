import random #allows program to generate a random number.
print("Welcome to the Number Guessing Game!🎉")
print("I'm thinking of a secret number between 1 and 100.")
print("Can you guess it? Let's find out! 😉")

#generates a random number(secret number).
scrt_number=random.randint(1,100)
attempts=0

#infinite loop
while True: #game keeps running until user guesses correctly.
    try: # to avoid errors if you accidentally type letters.
        guess=int(input("Make a guess:"))
        attempts+=1
        
        #compares guess with secret number 
        if guess<scrt_number:
            print("It's too low.Try again.")
        elif guess>scrt_number:
            print("It's too high.Try again.") 
        else:
            print(f"Congratulations! 🎉 You guessed it in {attempts} attempts.😊🙌 ")
            break
    except ValueError:
        print("Invalid! Please enter a valid number.")              