# ai-knowledge-assistant

An AI knowledge assistant that answers questions about a private knowledge base and cites its sources. Built in public, one small step at a time, as part of the "Dev to AI Engineer" learn-along.

## Status
04-10-2026: scaffolding and one typed model, no AI or API code yet.
08-10-2026: tests, ruff and a cleaner layout (exercises are separate from the package).

## Layout
```
src/ai_knowledge_assistant/   the package (real code only)
tests/                        pytest tests, no network and no API key
exercises/                    lesson practice, not part of the package
```

## Run the checks
```
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy
```
`uv run python exercises/practice_types.py` runs the Day 1 exercise.
`exercises/broken.py` is wrong on purpose: `uv run mypy exercises/broken.py` shows what mypy finds.
