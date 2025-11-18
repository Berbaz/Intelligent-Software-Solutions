# sort_manual.py
from typing import List, Dict, Any

def sort_dicts_by_key_manual(items: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Manual implementation:
    - Separates items that have the key from those that don't
    - Sorts the ones that have the key
    - Appends the ones without the key to the end (stable)
    """
    with_key = [d for d in items if key in d]
    without_key = [d for d in items if key not in d]

    # Use Timsort (Python's sorted) but show explicit comparator
    with_key_sorted = sorted(with_key, key=lambda d: d[key], reverse=reverse)
    return with_key_sorted + without_key


if __name__ == "__main__":
    data = [{"name":"a","score":10}, {"name":"b","score":5}, {"name":"c"}]
    print(sort_dicts_by_key_manual(data, "score"))
