import random  # To generate random numbers

def play_game(best_score=None):
    
    #Function to play one round of the number guessing game.
   # best_score: tracks the minimum attempts used across games
    #Returns the attempts used if the player wins, otherwise None
    
    number_to_guess = random.randint(1, 100)  # Computer picks a random number
    attempts_allowed = 7  # Maximum attempts
    attempts_used = 0

    print("\nI've picked a number between 1 and 100.")
    print(f"You have {attempts_allowed} attempts to guess it.")

    while attempts_used < attempts_allowed:
        try:
            guess_input = input(f"\nAttempt {attempts_used + 1}: Enter your guess: ").strip()
            
            if guess_input == "":
                print("You didn't enter anything. Please enter a number")
                continue

            guess = int(guess_input)  # Convert input to integer
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
                continue

        except ValueError:
            # Handles non-integer inputs
            print("Invalid input! Please enter a valid number between 1 to 100")
            continue

        attempts_used += 1  # Count this as an attempt

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts_used} attempts ")
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print(f" New best score! {best_score} attempts")
            return attempts_used  # Player won

        elif guess < number_to_guess:
            # Give hint if close
            if number_to_guess - guess <= 5:
                print(" Too low, but you're very close!")
            else:
                print(" Too low.")
        else:  # guess > number_to_guess
            if guess - number_to_guess <= 5:
                print(" Too high, but you're very close!")
            else:
                print(" Too high")

        print(f"Attempts remaining: {attempts_allowed - attempts_used}")

    # Player failed to guess
    print(f"\n You've used all attempts :( . The number was {number_to_guess}. Better luck next time! ")
    return None

def main():
    
    #Main function to control the game loop and track best score
    
    best_score = None  # Initialize best score

    print("Welcome to the Number Guessing Game!")

    while True:
        play_game(best_score)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        while play_again not in ("y", "n"):
            play_again = input("Please enter 'y' for yes or 'n' for no : ").strip().lower()
        if play_again == "n":
            print("Thanks for playing! ")
            break

# Run the game
if __name__ == "__main__":
    main()
