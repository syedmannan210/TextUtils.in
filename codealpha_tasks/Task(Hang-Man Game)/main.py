import random
import time


def hangman():
    print("Welcome To Hangman Game".center(150).upper())
    time.sleep(1)
    rules = f'''The Rules of the Game are:\n
  1) You have to guess the word letter vise.\n
  2) If you have guessed a single word correctly you'll win the game.\n
  3) If you did'nt guessed the word correctly, You'll lose a life.\n
  4) You have total of 5 lifes\n'''
    guide = input(
        "Do you want to know the rules of this game?(yes/no)\n").lower()
    if guide == "yes":
        print(rules)
    else:
        print("Seems like an expert! Lets proceed!\n")
    time.sleep(5)
    words = ["python", "java", "django", "kotlin"]
    guessed_words = []
    rand_word = random.choice(words)
    print(f'''Total letters in Word: {"_ " * len(rand_word)}''')
    if rand_word == "python":
        info = "Its a very famous programming language mainly used for machine learning and data science"
        print(f"Hint: {info}")
        {time.sleep(0.05)}
    elif rand_word == "java":
        info = "Very Famous Programming language used Desktop Applications"
        print(f"Hint: {info}")
        {time.sleep(0.05)}
    elif rand_word == "django":
        info = "Its a framework of very famous programming language for Web development"
        print(f"Hint: {info}")
        {time.sleep(0.05)}
    elif rand_word == "kotlin":
        info = "Programming language for Android Application Development"
        print(f"Hint: {info}")
        {time.sleep(0.05)}
    life = 5
    while life > 0:
        guess = input("Enter a letter of the Word!:\n").lower()
        if len(guess) != 1:
            print("Please Enter a single letter at a time:")
        elif guessed_words.count(guess) >= rand_word.count(guess) and guess in rand_word:
            print("You have already guessed this word!")
        elif guess not in rand_word:
            life = life - 1
            print(f"Incorrect Letter, You've got {life} lifes left!")

        else:
            {time.sleep(1)}
            print("Congratulations you have guessed a correct word\n")
            guessed_words.append(guess)
            # Check if the guessed letters are the same as the random word
            if set(guessed_words) == set(rand_word):
                {time.sleep(5)}
                print(f"{'-' * 32} You have won the game! {'-' * 32}".center(150))
                print(f"{'-' * 32} The word was \"{str(rand_word)}\" {'-' * 32}".center(150))
                break
    else:
        print(f"{'-'*32} You've got {life} lifes, You've lost! {'-'*32}".center(150))


if __name__ == "__main__":
    hangman()
