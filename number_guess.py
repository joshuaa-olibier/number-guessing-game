import random
import time


def game():
    print("=== NUMBER GUESSER PRO ===")
    secret = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while True:
        try:
            guess = int(input("Guess (1-100): "))
            attempts += 1

            if guess == secret:
                end_time = time.time()
                print(f"Correct! Time: {round(end_time - start_time, 2)}s | Attempts: {attempts}")
                break
            print("Too high!" if guess > secret else "Too low!")

        except ValueError:
            print("Numbers only!")


if __name__ == "__main__":
    game()
    input("Press Enter to exit...")