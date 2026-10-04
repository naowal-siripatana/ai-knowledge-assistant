import re
from collections import Counter


def word_count(text: str) -> int:
    # Count the number of words in the given text
    if not isinstance(text, str):
        raise TypeError(f"word_count expects 'str', got {type(text).__name__}")
    return len(text.split())

def top_n_words(text: str, n: int = 5) -> list[str]:
    # Return the top `n` most frequent words (case-insensitive, punctuation removed)
    # Use a regex to extract word tokens and normalize to lower-case.
    if not isinstance(text, str):
        raise TypeError(f"top_n_words expects 'text: str', got {type(text).__name__}")
    if not isinstance(n, int):
        raise TypeError(f"top_n_words expects 'n: int', got {type(n).__name__}")
    words = re.findall(r"\b\w+\b", text.lower())
    # Use Counter to both count and sort in one call
    return [word for word, _ in Counter(words).most_common(n)]

def find_user(users: dict[str, str], user_id: str) -> str | None:
    # Find a user by their ID and return their information, or None if not found
    # `dict.get` already returns None when the key is missing.
    if not isinstance(users, dict):
        raise TypeError(f"find_user expects 'users: dict[str,str]', got {type(users).__name__}")
    if not isinstance(user_id, str):
        raise TypeError(f"find_user expects 'user_id: str', got {type(user_id).__name__}")
    return users.get(user_id)

if __name__ == "__main__":
    text = "the cat and the dog and the bird"
    print(word_count(text))
    print(top_n_words(text, 2))
    users = {"1": "Ann", "2": "Bob"}
    print(find_user(users, "1"))
    print(find_user(users, "9"))

    # Wrong-typed calls: hints alone are not enforced at runtime
    try:
        find_user(users, 1)  # type: ignore[arg-type]
    except TypeError as e:  # raised by our manual isinstance guard, not by the hint
        print("TypeError:", e)
    try:
        word_count(123)  # type: ignore[arg-type]
    except TypeError as e:
        print("TypeError:", e)

    # A type hint is a promise to readers and tools (mypy, editor); Python itself never checks it.
