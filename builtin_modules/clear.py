import os
import sys

def clear(text: str) -> None:
    if os.name in ('nt', 'dos'):
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')
