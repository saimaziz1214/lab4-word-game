import random

# ─── Word List ───────────────────────────────────────────────────────────────

WORDS = [
    "python", "hangman", "computer", "science", "engineer",
    "keyboard", "variable", "function", "algorithm", "recursion",
    "iteration", "debugging", "testing", "software", "hardware",
]

# ─── Pure Logic Layer (no print statements here) ──────────────────────────────

def pick_word(words: list[str]) -> str:
    """Return a random word from the word list."""
    return random.choice(words)


def update_game_state(
    secret_word: str,
    guessed_letters: list[str],
    guess: str,
    lives: int,
) -> tuple[list[str], int]:
    """Process a player's letter guess and update game variables.

    The caller maintains the list of letters that have been guessed so far and
    the number of remaining lives.  This function normalises the incoming
    guess to lowercase, ignores duplicates, and decrements ``lives`` when the
    guess is not present in ``secret_word``.

    Returns a tuple containing the updated list of guessed letters and the
    possibly adjusted lives count.  The secret word itself is left unchanged;
    another helper can use the returned ``guessed_letters`` to construct the
    visible display (e.g. "_ a _ _").
    """
    # normalise the guess so that 'A' and 'a' are treated the same
    guess = guess.lower()

    # if the player has already tried this letter do nothing
    if guess in guessed_letters:
        return guessed_letters, lives

    # record the new guess
    guessed_letters = guessed_letters + [guess]

    # lose a life only on incorrect guesses
    if guess not in secret_word:
        lives -= 1

    return guessed_letters, lives


def build_masked_word(secret_word: str, guessed_letters: list[str]) -> list[str]:
    """
    Return a list of characters: revealed letter if guessed, '_' otherwise.
    No string replacement functions used.
    """
    return [ch if ch in guessed_letters else "_" for ch in secret_word]


def is_win(secret_word: str, guessed_letters: list[str]) -> bool:
    """True when every letter in secret_word has been guessed."""
    return all(ch in guessed_letters for ch in secret_word)


def is_loss(lives: int) -> bool:
    """True when the player has no lives remaining."""
    return lives <= 0


def get_wrong_guesses(secret_word: str, guessed_letters: list[str]) -> list[str]:
    """Return letters that were guessed but are not in the secret word."""
    return [ch for ch in guessed_letters if ch not in secret_word]


# ─── UI / Display Layer ───────────────────────────────────────────────────────

def display_state(secret_word: str, guessed_letters: list[str], lives: int) -> None:
    masked = build_masked_word(secret_word, guessed_letters)
    wrong = get_wrong_guesses(secret_word, guessed_letters)
    print("\n" + " ".join(masked))
    print(f"Lives remaining : {lives}")
    print(f"Wrong guesses   : {', '.join(wrong) if wrong else 'none'}")
    print(f"Guessed so far  : {', '.join(sorted(guessed_letters)) if guessed_letters else 'none'}")


def get_guess(guessed_letters: list[str]) -> str:
    """Prompt until the player enters a valid, new single letter."""
    while True:
        raw = input("\nGuess a letter: ").strip().lower()
        if len(raw) != 1 or not raw.isalpha():
            print("Please enter a single letter.")
        elif raw in guessed_letters:
            print(f"You already guessed '{raw}'. Try another.")
        else:
            return raw


def display_result(secret_word: str, won: bool) -> None:
    if won:
        print(f"\n🎉 You won! The word was '{secret_word}'.")
    else:
        print(f"\n💀 Game over! The word was '{secret_word}'.")


def ask_replay() -> bool:
    """Return True if the player wants to play again."""
    answer = input("\nPlay again? (y/n): ").strip().lower()
    return answer == "y"


# ─── Game Loop (no while True) ────────────────────────────────────────────────

def play_turn(secret_word: str, guessed_letters: list[str], lives: int) -> None:
    """Recursive turn loop — replaces while True."""
    display_state(secret_word, guessed_letters, lives)

    if is_win(secret_word, guessed_letters):
        display_result(secret_word, won=True)
        return
    if is_loss(lives):
        display_result(secret_word, won=False)
        return

    guess = get_guess(guessed_letters)
    new_guessed, new_lives = update_game_state(secret_word, guessed_letters, guess, lives)

    if guess in secret_word:
        print(f"✓ '{guess}' is in the word!")
    else:
        print(f"✗ '{guess}' is not in the word.")

    play_turn(secret_word, new_guessed, new_lives)


def play_game(max_lives: int = 6) -> None:
    """Start a single game."""
    secret_word = pick_word(WORDS)
    print(f"\nNew game! The word has {len(secret_word)} letters. You have {max_lives} lives.")
    play_turn(secret_word, [], max_lives)


def run(max_lives: int = 6) -> None:
    """Entry point — supports replay without restarting the program."""
    print("=== Guess The Word ===")
    play_game(max_lives)
    if ask_replay():
        run(max_lives)
    else:
        print("\nThanks for playing. Goodbye!")


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run()