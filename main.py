import random
import string

# ─── Word List ─────────────────────────────────────────

WORDS = [
    "python", "hangman", "computer", "science", "engineer",
    "keyboard", "variable", "function", "algorithm", "recursion",
    "iteration", "debugging", "testing", "software", "hardware",
]

# ─── Logic Functions ───────────────────────────────────

def pick_word(words):
    return random.choice(words)


def update_game_state(secret_word, guessed_letters, guess, lives):

    guess = guess.lower()

    if guess in guessed_letters:
        return guessed_letters, lives

    guessed_letters = guessed_letters + [guess]

    if guess not in secret_word:
        lives = lives - 1

    return guessed_letters, lives


def build_masked_word(secret_word, guessed_letters):

    result = []

    for ch in secret_word:
        if ch in guessed_letters:
            result.append(ch)
        else:
            result.append("_")

    return result


def is_win(secret_word, guessed_letters):

    for ch in secret_word:
        if ch not in guessed_letters:
            return False

    return True


def is_loss(lives):

    if lives <= 0:
        return True

    return False


def get_wrong_guesses(secret_word, guessed_letters):

    wrong = []

    for ch in guessed_letters:
        if ch not in secret_word:
            wrong.append(ch)

    return wrong


# ─── Auto Player ───────────────────────────────────────

def auto_guess(guessed_letters):

    alphabet = list(string.ascii_lowercase)

    while True:

        guess = random.choice(alphabet)

        if guess not in guessed_letters:
            return guess


# ─── Display Functions ─────────────────────────────────

def display_state(secret_word, guessed_letters, lives):

    masked = build_masked_word(secret_word, guessed_letters)
    wrong = get_wrong_guesses(secret_word, guessed_letters)

    print("\n" + " ".join(masked))
    print("Lives remaining:", lives)

    if wrong:
        print("Wrong guesses:", ", ".join(wrong))
    else:
        print("Wrong guesses: none")

    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))
    else:
        print("Guessed letters: none")


def get_guess(guessed_letters):

    while True:

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Enter one letter only.")

        elif not guess.isalpha():
            print("Enter a letter.")

        elif guess in guessed_letters:
            print("You already guessed that.")

        else:
            return guess


def display_result(secret_word, won):

    if won:
        print("\nYou won! The word was:", secret_word)
    else:
        print("\nGame over. The word was:", secret_word)


def ask_replay():

    answer = input("\nPlay again? (y/n): ").strip().lower()

    if answer == "y":
        return True

    return False


# ─── Player Game Loop ──────────────────────────────────

def play_turn(secret_word, guessed_letters, lives):

    display_state(secret_word, guessed_letters, lives)

    if is_win(secret_word, guessed_letters):
        display_result(secret_word, True)
        return

    if is_loss(lives):
        display_result(secret_word, False)
        return

    guess = get_guess(guessed_letters)

    new_guessed, new_lives = update_game_state(
        secret_word,
        guessed_letters,
        guess,
        lives
    )

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")

    play_turn(secret_word, new_guessed, new_lives)


def play_game(max_lives=6):

    secret_word = pick_word(WORDS)

    print("\nNew game started.")
    print("Word has", len(secret_word), "letters.")

    play_turn(secret_word, [], max_lives)


# ─── Auto Play Loop ────────────────────────────────────

def auto_play_turn(secret_word, guessed_letters, lives):

    display_state(secret_word, guessed_letters, lives)

    if is_win(secret_word, guessed_letters):
        display_result(secret_word, True)
        return

    if is_loss(lives):
        display_result(secret_word, False)
        return

    guess = auto_guess(guessed_letters)

    print("\nComputer guesses:", guess)

    new_guessed, new_lives = update_game_state(
        secret_word,
        guessed_letters,
        guess,
        lives
    )

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")

    auto_play_turn(secret_word, new_guessed, new_lives)


def auto_play_game(max_lives=6):

    secret_word = pick_word(WORDS)

    print("\nAuto Play Mode")
    print("Word has", len(secret_word), "letters.")

    auto_play_turn(secret_word, [], max_lives)


# ─── Menu ──────────────────────────────────────────────

def choose_mode():

    print("\nChoose mode:")
    print("1 - Play the game")
    print("2 - Auto Play")

    choice = input("Enter 1 or 2: ")

    return choice


def run(max_lives=6):

    print("=== Guess The Word ===")

    mode = choose_mode()

    if mode == "1":
        play_game(max_lives)

    elif mode == "2":
        auto_play_game(max_lives)

    else:
        print("Invalid choice")

    if ask_replay():
        run(max_lives)
    else:
        print("\nGoodbye!")


# ─── Entry Point ───────────────────────────────────────

if __name__ == "__main__":
    run()