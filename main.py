import asyncio
import sys
import os
import builtin_modules
from help_console import help_shell

from builtin_modules import echo, get_history

builtin_modules_names = ['history', 'help', 'echo', 'test']

async def shell(history=[]):
    while True:
        try:
            text = input('>>> ')
        except EOFError or KeyboardInterrupt:
            sys.exit(0)

        if text == None:
            await shell()
        else:
            history.append(text)

        if text == 'history':
            get_history(history)

        if text == 'help':
            help_res = await help_shell()
            print(help_res)

        if text.split(' ')[0] in builtin_modules_names:
            x = getattr(builtin_modules, text.split(' ')[0])
            x(text)

        if text == '.exit':
            sys.exit(0)

def clear_console():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')

__version__ = '0.0.1-alpha'

def main():
    try:
        clear_console()
        print(f'DonutShell v{__version__}')
        asyncio.run(shell())
    except EOFError or KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main()
