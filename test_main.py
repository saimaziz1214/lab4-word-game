import pytest
from main import (
    update_game_state,
    build_masked_word,
    is_win,
    is_loss,
    get_wrong_guesses,
)

# ─── update_game_state ────────────────────────────────────────────────────────

def test_correct_guess_does_not_lose_life():
    _, lives = update_game_state("python", [], "p", 6)
    assert lives == 6

def test_wrong_guess_loses_a_life():
    _, lives = update_game_state("python", [], "z", 6)
    assert lives == 5

def test_correct_guess_added_to_guessed_letters():
    guessed, _ = update_game_state("python", [], "p", 6)
    assert "p" in guessed

def test_wrong_guess_added_to_guessed_letters():
    guessed, _ = update_game_state("python", [], "z", 6)
    assert "z" in guessed

def test_duplicate_guess_does_not_change_state():
    guessed, lives = update_game_state("python", ["p"], "p", 6)
    assert lives == 6
    assert guessed.count("p") == 1

def test_guess_is_case_insensitive():
    guessed, lives = update_game_state("python", [], "P", 6)
    assert "p" in guessed
    assert lives == 6

def test_original_list_not_mutated():
    original = ["p"]
    update_game_state("python", original, "y", 6)
    assert original == ["p"]

# ─── build_masked_word ────────────────────────────────────────────────────────

def test_no_letters_guessed_all_underscores():
    assert build_masked_word("cat", []) == ["_", "_", "_"]

def test_all_letters_guessed_reveals_word():
    assert build_masked_word("cat", ["c", "a", "t"]) == ["c", "a", "t"]

def test_partial_guess_reveals_correct_positions():
    assert build_masked_word("cat", ["a"]) == ["_", "a", "_"]

def test_repeated_letter_in_word_all_revealed():
    assert build_masked_word("banana", ["a", "b"]) == ["b", "a", "_", "a", "_", "a"]

# ─── is_win ───────────────────────────────────────────────────────────────────

def test_win_when_all_letters_guessed():
    assert is_win("cat", ["c", "a", "t"]) is True

def test_no_win_when_letters_missing():
    assert is_win("cat", ["c", "a"]) is False

def test_win_with_extra_wrong_guesses():
    assert is_win("cat", ["c", "a", "t", "z", "x"]) is True

# ─── is_loss ──────────────────────────────────────────────────────────────────

def test_loss_when_lives_zero():
    assert is_loss(0) is True

def test_loss_when_lives_negative():
    assert is_loss(-1) is True

def test_no_loss_when_lives_remaining():
    assert is_loss(3) is False

# ─── get_wrong_guesses ────────────────────────────────────────────────────────

def test_wrong_guesses_identified_correctly():
    assert get_wrong_guesses("cat", ["c", "a", "t", "z"]) == ["z"]

def test_no_wrong_guesses():
    assert get_wrong_guesses("cat", ["c", "a", "t"]) == []

def test_all_wrong_guesses():
    result = get_wrong_guesses("cat", ["x", "y", "z"])
    assert sorted(result) == ["x", "y", "z"]