"""Day 1 exercise: typed functions. Run: uv run python exercises/practice_types.py"""

import re
from collections import Counter


def word_count(text: str) -> int:
    return len(text.split())


def top_n_words(text: str, n: int = 5) -> list[str]:
    words = re.findall(r"\b\w+\b", text.lower())
    return [word for word, _ in Counter(words).most_common(n)]


def find_user(users: dict[str, str], user_id: str) -> str | None:
    return users.get(user_id)


if __name__ == "__main__":
    text = "the cat and the dog and the bird"
    print(word_count(text))
    print(top_n_words(text, 2))
    users = {"1": "Ann", "2": "Bob"}
    print(find_user(users, "1"))
    print(find_user(users, "9"))
