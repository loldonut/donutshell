from typing import List

def get_history(history: List[str]) -> str:
    res = ''
    for x in history:
        res += x.join('\n')
    return res
