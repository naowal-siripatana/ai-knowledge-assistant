from ai_knowledge_assistant.documents import Document, truncate_preview, word_count


def make_doc(body: str) -> Document:
    return Document(doc_id="1", title="Guide", body=body, source="manual.md")


def test_word_count() -> None:
    assert word_count(make_doc("one two three")) == 3


def test_preview_cuts_long_text() -> None:
    assert truncate_preview(make_doc("a b c d"), max_words=2) == "a b..."


def test_preview_keeps_short_text() -> None:
    assert truncate_preview(make_doc("a b"), max_words=5) == "a b"
