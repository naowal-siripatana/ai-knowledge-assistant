from dataclasses import dataclass


@dataclass
class Document:
    doc_id: str
    title: str
    body: str
    source: str


def word_count(doc: Document) -> int:
    return len(doc.body.split())


def truncate_preview(doc: Document, max_words: int = 20) -> str:
    words = doc.body.split()
    preview = " ".join(words[:max_words])
    return preview + ("..." if len(words) > max_words else "")
