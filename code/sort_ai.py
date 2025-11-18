# sort_ai.py
from typing import List, Dict, Any

def sort_dicts_by_key_ai(items: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    AI-suggested implementation: uses Python's built-in sorted with a lambda key.
    Returns a NEW list sorted by the specified key.
    If a dictionary is missing the key, treat it as None (which sorts at the end).
    """
    return sorted(items, key=lambda d: d.get(key, None), reverse=reverse)


# Example usage
if __name__ == "__main__":
    data = [{"name":"a", "score":10}, {"name":"b","score":5}, {"name":"c"}]
    print(sort_dicts_by_key_ai(data, "score"))
