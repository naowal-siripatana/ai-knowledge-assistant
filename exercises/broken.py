"""Day 1 exercise: wrong-typed calls on purpose. Run mypy on it to see both mistakes.

Python runs this without complaint, then fails inside word_count. mypy flags both
calls before anything runs: uv run mypy exercises/broken.py
"""

from practice_types import find_user, word_count

users = {"1": "Ann", "2": "Bob"}
print(find_user(users, 1))
print(word_count(123))
