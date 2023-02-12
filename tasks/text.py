from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    res = text.split()
    if not res:
        return None, None
    a1 = min((word for word in res if word), key=len)
    a2 = max((word for word in res if word), key=len)

    return a1, a2
