from ai_knowledge_assistant.practice_types import word_count, find_user

# Intentional wrong-typed calls to demonstrate mypy

def bad_calls() -> None:
    word_count(123)         # error: Argument 1 to "word_count" has incompatible type "int"; expected "str"
    find_user({"1": "Ann"}, 1)  # error: Argument 2 to "find_user" has incompatible type "int"; expected "str"


bad_calls()
