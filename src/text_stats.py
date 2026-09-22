"""Count lines, words, and characters in a UTF-8 text file."""

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Dict, List


def calculate_stats(text: str) -> Dict[str, object]:
    """Return line, word, and character counts for text."""
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def most_common_words(text: str, limit: int) -> List[Dict[str, object]]:
    """Return the most frequent words, ordered by count and then word."""
    counts = Counter(word.casefold() for word in text.split())
    return [
        {"word": word, "count": count}
        for word, count in sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )[:limit]
    ]


def main() -> None:
    """Read the file supplied on the command line and print JSON statistics."""
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a UTF-8 text file."
    )
    parser.add_argument("file", type=Path, help="path to a UTF-8 text file")
    parser.add_argument(
        "--top",
        type=int,
        metavar="N",
        help="include the N most frequent words in the JSON output",
    )
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    stats = calculate_stats(text)
    if args.top is not None:
        if args.top < 0:
            parser.error("--top must be non-negative")
        stats["top"] = most_common_words(text, args.top)
    print(json.dumps(stats, sort_keys=True))


if __name__ == "__main__":
    main()
