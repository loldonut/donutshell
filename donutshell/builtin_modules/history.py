from typing import List


def history(text: str, history: List[str]) -> None:
    res = ''
    for i, v in enumerate(history):
        res += v + ('\n' if i != (len(history) - 1) 
                                else '')

    print(res)
