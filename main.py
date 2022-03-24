import asyncio
import sys
import os
import builtin_modules
from help_console import help_shell

builtin_modules_names = ['help', 'echo', 'test']

async def shell(history=[]) -> None:
    while True:
        try:
            cwd = os.getcwd().split('/')
            text = input(f'{cwd[len(cwd) - 1]} >>> ')
        except EOFError or KeyboardInterrupt:
            sys.exit(0)

        if text.strip() == "":
            await shell()
        else:
            history.append(text)

        if text == 'help':
            help_res = await help_shell()
            print(help_res)
            await shell()

        if text == 'history':
            res = ''
            for i, v in enumerate(history):
                res += v + ('\n' if i != (len(history) - 1) else '')
            print(res)
            await shell()

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

__version__ = '0.0.1'

def main():
    try:
        clear_console()
        print(f'DonutShell v{__version__}')
        asyncio.run(shell())
    except EOFError or KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main()
