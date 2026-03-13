My Original Thinking
--App States
Game starts with a hidden word and empty guesses
Player is actively guessing letters (playing state)
Game ends in a win (word fully revealed) or a loss (no lives left)
After game ends, player can choose to replay

--App Variables
The secret word
The masked/display version of the word (blanks for unguessed letters)
A list of guessed letters
Number of remaining lives (default 6)
Game status (ongoing / won / lost)

--App Rules and Invariants
Player guesses one letter at a time
Correct guess reveals all matching positions in the word
Wrong guess costs one life
Guesses must be a single letter, not previously guessed, case-insensitive
Lives stay between 0 and the maximum — never go negative
The secret word never changes during a game
No letter can be guessed more than once
The display string always has the same length as the secret word

--App Bugs
Duplicate guesses allowed if not checked — player could lose a life for guessing the same letter twice
Case sensitivity issues — 'A' and 'a' treated as different letters if input not normalized
Incorrect display updates — letters not revealed in all correct positions
Win/loss not detected properly — game continues after it should have ended
Invalid input accepted — non-letters, multiple letters, or empty string not handled
Words with repeated letters — masked word might not reveal all positions
Edge cases — very short words (1 letter), words with special characters
Recursion depth — if using recursion instead of while loops, deep recursion could cause a stack overflow (not a real risk with 6 lives but worth knowing)


CoPilot Suggestions
App States
CoPilot described these states when asked directly:

Initial/Setup State — secret word chosen, display initialized with blanks, guessed letters empty, attempts set to max
Guessing/Playing State — player actively guessing, display updates after each guess, win/loss checked each turn
Won State — word fully revealed before attempts ran out
Lost State — attempts reached zero, word not fully guessed
Game Over State — general end state (win or loss), no more guesses accepted, full word revealed

Observation: CoPilot's breakdown was more formal than mine but matched my thinking. The "Game Over" state as a wrapper for won/lost is a useful distinction for cleaner code structure.
App Variables
CoPilot suggested tracking:

The secret word (string)
Current display of the word (blanks for unguessed letters)
A list or set of guessed letters
Number of remaining attempts (starting at 6)
Game status ("ongoing", "won", or "lost")

Observation: CoPilot suggested using a set instead of a list for guessed letters — sets automatically prevent duplicates. I kept a list to preserve guess order for display purposes.
App Rules and Invariants
CoPilot confirmed my list and added:

The display string must always match the length of the secret word
Game status is always one of: ongoing, won, lost — no other values allowed

Observation: CoPilot was thorough here and didn't overcomplicate it. The invariants matched what I had already thought of.
App Bugs
CoPilot added several bugs I hadn't fully considered:

Display formatting — extra spaces, wrong underscores, or not showing the full word at game end
Word length mismatches — if secret word has spaces or hyphens, the display breaks
Infinite recursion — if the win/loss base case is never reached

Added full implementation and docstring for `update_game_state`, then reviewed its behavior with suggestions for display helper and testing.



App Rules and Invariants
CoPilot confirmed my list and added:
- The display string must always match the length of the secret word
- Game status is always one of: ongoing, won, lost — no other values allowed


 App Bugs
CoPilot added several bugs I hadn't fully considered:
-Display formatting — extra spaces, wrong underscores, or not showing the full word at game end
- Word length mismatches — if secret word has spaces or hyphens, the display breaks
- Infinite recursion — if the win/loss base case is never reached


---

#Testing

 Tests Written
Tests were written for all core logic functions using `pytest`:
- `update_game_state` — 7 tests
- `build_masked_word` — 4 tests
- `is_win` — 3 tests
- `is_loss` — 3 tests
- `get_wrong_guesses` — 3 tests
- Total: 20 tests

What the Tests Cover
- Correct guess does not cost a life
- Wrong guess costs exactly one life
- Duplicate guess is ignored — no life lost, not added twice
- Case insensitivity — 'P' and 'p' treated as the same letter
- Immutability — original guessed_letters list is never mutated
- Masked word builds correctly for partial, full, and repeated letters
- Win detection when all letters guessed
- Loss detection when lives reach zero or below
- Wrong guesses tracked correctly

-How to Run the Tests
```bash
python3 -m pytest test_main.py -v
```

 Testing Experience
- Asked CoPilot to suggest tests for `update_game_state` — it gave a good starting list covering the main cases
- CoPilot suggested using `pytest` which required installing it separately
- Had trouble running `pytest` directly on Mac — `zsh: command not found: pytest` — had to use `python3 -m pytest` instead
- The `test_main.py` file was empty at first (0 bytes) because it had not been copied into the project folder correctly

---

Notes on the CoPilot Interaction

 General Observations
- CoPilot started in Socratic mode — it responded to questions with more questions rather than direct answers. This was frustrating at first but pushed me to think before getting answers.
- When I explicitly asked for direct answers, CoPilot switched modes and became much more useful immediately.
- The quality of answers improved significantly when questions were specific (e.g. "what are the rules and invariants?") vs. vague (e.g. "what do you think?").
- CoPilot did not automatically update the journal — it had to be explicitly prompted multiple times.

 CoPilot Free Version Ran Out
- During the testing phase, my free CoPilot quota ran out mid-session.
- I could no longer use CoPilot to ask questions or generate suggestions.
- I switched to another AI tool (Claude) to continue getting help with the remaining parts of the project — including generating the tests, completing `main.py`, and writing the documentation files.
- This was an interesting real-world limitation: AI tools have usage caps, and knowing when to switch tools or work independently is an important skill.
- The switch between tools was mostly seamless — the prompting approach was similar, though Claude was more willing to give direct answers without needing to explicitly disable a Socratic mode.