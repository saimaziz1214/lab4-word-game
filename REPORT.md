# The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

# First Impressions - Initial Take on the Project Assignment
## In this section, students will provide their initial thoughts on the project assignment, including their understanding of the requirements, any assumptions they made, points that need clarification, and their overall approach to tackling the project.
## Initial Thoughts
## Assumptions Made
## Points Needing Clarification

# Key Learnings
## Here, students will summarize the most important things they learned while working on the project. This could include computer science related concepts, technical skills, insights about using CoPilot effectively, and any new concepts or tools they encountered
## Computer Science Concepts and Technical Skills
## Insights about Using CoPilot Effectively
## New Concepts or Tools Encountered

# Report on CoPilot Prompting Experience
## Student may pull examples from the JOURNAL.md to illustrate their experience, including specific interactions that were particularly helpful or challenging.
### Types of prompts that worked well
### Types of prompts that did not work well or failed

# Limitations, Hallucinations and Failures
## In this section, students will document any instances where CoPilot provided incorrect or misleading information (hallucinations) or where it failed to provide a useful response. They will analyze why these issues occurred and how they impacted their work on the project.
## For example: Fabricated APIs, Deprecated functions, Subtle logical errors, Confident but wrong explanations, Over-engineered solutions, Under-engineered solutions, overcomplicated code, oversimplified code, etc.
## Examples of Hallucinations or Failures or Misleading Information or Confident but Wrong Explanations, or Over-engineered or Under-engineered Solutions
## Analysis of Why These Issues Occurred
## Impact on the Project

# AI Trust
## When did I trust the AI?
## When did I stop trusting it?
## What signals or situations or patterns indicated low reliability?

# What I Learned
## What did you learn about software development?
## What did you learn about using AI tools?
## When should you trust AI? When should you double-check it?

# Reflection
## Did AI make you faster? Why or why not?
## Did you feel in control of the code?
## Would you use AI the same way next time? What would you change?






# Project Report — Guess The Word

---

# First Impressions

## Initial Thoughts

When I first read the assignment, Hangman seemed straightforward — it is a well-known game and the logic is not complicated. What made it more interesting were the constraints: no `while True` loops, no string replacement functions, logic and UI fully separated, and replay support without restarting the program. These were not obvious restrictions at first, but they forced a cleaner design than I would have written naturally.

The assignment also required design thinking before coding — writing down states, variables, rules, and bugs before touching any code. This felt slow at first but turned out to be genuinely useful. Having that foundation made the implementation phase much clearer.

## Assumptions Made

- "No `while True`" means recursion is the intended alternative for the game loop.
- "No string replacement functions" means `.replace()` is off limits — the masked word needs to be built by checking each character individually.
- The word list could be hardcoded for this scope — no external file or API needed.
- The journal and markdown files are meant to capture the process honestly, not just the final result.

## Points Needing Clarification

- Whether recursion counts as a "loop" in spirit — it does not, and it satisfies the constraint cleanly.
- Whether tests needed to be in a separate file — went with `test_main.py` using `pytest` as a standard convention.
- How detailed the REPORT.md needed to be — the template made this clear once I read it carefully.

---

# Key Learnings

## Computer Science Concepts and Technical Skills

- **Pure functions:** Writing `update_game_state` as a pure function — no side effects, no mutation, returns new state — made it much easier to test and reason about. If a function has no side effects, you can test it with a single line.
- **Recursion vs iteration:** Using recursion for the game loop instead of `while True` forced a clearer mental model. Each recursive call represents one turn. The base cases are win and loss. This is cleaner than managing a loop condition manually.
- **Immutability:** Returning `guessed_letters + [guess]` instead of mutating with `.append()` prevents subtle bugs where the caller's list gets modified unexpectedly. This was caught during the CoPilot review phase.
- **Separation of concerns:** Keeping all `print()` and `input()` calls out of the logic layer makes the logic fully testable without needing to mock user input. Logic functions return values; UI functions handle display.
- **Testing with pytest:** Writing 20 tests across 5 functions covered edge cases that are easy to miss — repeated letters, case sensitivity, duplicate guesses, and list immutability.

## Insights about Using CoPilot Effectively

- Specific prompts get much better results than vague ones. "What are the rules and invariants of a Hangman game?" produced a useful, structured answer. "What do you think?" produced another question back.
- CoPilot works well as a reviewer. Asking it to review `update_game_state` immediately caught the mutation bug.
- CoPilot works well for generating test cases — it suggested edge cases I had not thought of.
- CoPilot's Socratic mode, while frustrating at first, did serve a purpose — it pushed me to think before getting answers rather than just accepting whatever was generated.

## New Concepts or Tools Encountered

- `pytest` — clean Python testing framework. Requires `python3 -m pytest` on Mac rather than just `pytest` due to PATH issues.
- Python virtual environments (`venv`) for isolating dependencies.
- The difference between `list.append()` (mutates in place) and `list + [item]` (returns new list) — a subtle but important distinction for writing pure functions.

---

# Report on CoPilot Prompting Experience

## Types of Prompts That Worked Well

- **"What are the rules and invariants?"** — produced a clear, structured list that was immediately useful for MY_NOTES.md.
- **"What are possible bugs in a Hangman implementation?"** — produced a practical checklist of things to watch out for, several of which I had not considered.
- **"Can you review my `update_game_state` function?"** — specific and targeted, got actionable feedback including the mutation bug catch.
- **"Can you suggest tests for this function?"** — produced a solid set of test cases quickly covering the main scenarios.
- **"I need direct answers"** — explicitly disabling Socratic mode immediately improved the quality and usefulness of responses.

## Types of Prompts That Did Not Work Well

- **"What do you think?"** — too vague, CoPilot responded with more questions instead of useful content.
- **"I need to make a plan"** — similarly vague, did not produce actionable output until I gave more specific context.
- **"Update the journal"** — had to be asked multiple times before the journal actually got updated. The agent did not trigger reliably.
- Early prompts before disabling Socratic mode were largely unproductive — CoPilot kept redirecting instead of answering.

---

# Limitations, Hallucinations and Failures

## Examples of Failures or Misleading Information

- **Socratic mode by default:** CoPilot's default Socratic behavior meant that early questions were met with more questions rather than answers. This is a pedagogical choice by the professor, but in practice it felt like a limitation when trying to make progress efficiently.
- **Journal agent unreliable:** The journal-logger agent did not update automatically after every interaction as intended. It had to be explicitly triggered multiple times, and even then sometimes did not capture the full conversation history correctly.
- **CoPilot free version quota ran out:** Mid-project, the free CoPilot quota was exhausted. This completely blocked further use of CoPilot for the remainder of the session.
- **`while True` and `.replace()` suggestions:** In early drafts, CoPilot suggested patterns that directly violated the assignment constraints — `while True` loops and `.replace()` for the masked word. These had to be explicitly flagged and corrected.

## Analysis of Why These Issues Occurred

- CoPilot does not automatically know the constraints of a specific assignment unless they are stated in every prompt. It defaults to the most common, idiomatic Python patterns — which happen to be `while True` and `.replace()` in this case.
- The journal agent failure was likely a configuration issue with the `.github/agents` setup rather than a CoPilot reasoning failure.
- The free quota running out is simply a product limitation — not a reliability issue, but a real constraint that affected the workflow.

## Impact on the Project

- The constraint violations were caught early and corrected before they made it into the final code — low impact.
- The journal agent failures meant the JOURNAL.md had gaps that needed to be filled in manually.
- The free version running out was the most significant impact — it forced a switch to a different AI tool (Claude) to complete the project. Interestingly, this was a useful experience: it showed that prompting skills transfer across different AI tools, and that knowing when to switch tools is itself a valuable skill.

---

# AI Trust

## When Did I Trust the AI?

- When it identified the mutation bug in `update_game_state` — the reasoning was correct and easy to verify by reading the code.
- When it suggested test cases — these were straightforward to verify by running them.
- When it explained concepts like pure functions and immutability — these matched what I already knew or could look up.
- When Claude generated the full `main.py` — I read through it, understood each function, and verified the constraints were met before using it.

## When Did I Stop Trusting It?

- When CoPilot suggested `while True` and `.replace()` patterns that directly violated the assignment constraints — this was a clear signal that it was not aware of the specific rules.
- When the journal agent claimed to have updated the journal but had not actually done so — trust dropped significantly after this happened more than once.

## What Signals or Situations Indicated Low Reliability?

- Output that contradicted stated constraints — if I said "no while True" and the suggestion used `while True`, something went wrong.
- Confident claims that could not be verified (e.g. "the journal has been updated") without checking the actual file.
- Vague or circular responses — answering a question with another question when a direct answer was needed.

---

# What I Learned

## What Did You Learn About Software Development?

- Design before coding genuinely helps. Writing down states, variables, rules, and bugs before writing a line of code made the implementation faster and cleaner.
- Constraints clarify design. Being told "no `while True`" forced a better structure than I would have chosen on my own.
- Pure functions are easier to test. Separating logic from UI is not just good style — it has a direct practical benefit when writing tests.
- Testing catches bugs that code review misses. The immutability test caught a subtle bug that would have been hard to spot just by reading the code.

## What Did You Learn About Using AI Tools?

- AI is most useful as a reviewer and a collaborator, not as a code generator to blindly accept.
- The quality of AI output is directly proportional to the specificity of the prompt.
- AI tools have real limitations — usage quotas, default behaviors that conflict with specific requirements, and agents that do not always work as advertised.
- Prompting skills transfer across tools. Switching from CoPilot to Claude mid-project was mostly seamless because the same principles apply: be specific, give context, verify the output.

## When Should You Trust AI? When Should You Double-Check It?

- **High trust:** boilerplate code, syntax questions, generating test cases, explaining well-known concepts, code review feedback.
- **Always verify:** anything involving project-specific constraints, business logic, correctness of algorithms, and any claim the AI makes about actions it has taken (like updating a file).

---

# Reflection

## Did AI Make You Faster? Why or Why Not?

Yes, a lot faster. Every phase of the project moved quicker with AI assistance. The design thinking phase was faster because CoPilot rapidly generated comprehensive lists of states, variables, rules, and bugs — things that would have taken much longer to think through alone. The testing phase was faster because writing 20 test cases manually would have been tedious and slow. The documentation phase was faster because AI handles structured writing very well.

Even the coding phase was faster — having a working draft to read and verify is much quicker than starting from a blank file, even accounting for the time spent checking the output against the constraints.

## Did You Feel in Control of the Code?

Yes, fully in control. The design thinking phase at the start was key to this. Because I had already written down the states, variables, rules, and expected behavior before any code was written, I always had a clear picture of what the code should do. This meant I could read AI-generated code critically and spot when something was wrong — like when CoPilot suggested `while True` or `.replace()` in violation of the constraints.

Understanding the code before accepting it meant I owned it, not the AI.

## Would You Use AI the Same Way Next Time? What Would You Change?

Yes, the overall approach worked very well: think and design first → implement the core logic → use AI to review and improve → use AI for tests and documentation. I would keep this pattern.

The one thing I would change is managing the free quota better. The biggest challenge was CoPilot's free version running out mid-project, which forced an unexpected switch to another AI tool. Next time I would be more aware of how many requests I am using and save the quota for the most important interactions — code review and testing — rather than spending it on early exploratory questions that could be answered by thinking independently first.