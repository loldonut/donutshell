import asyncio
import sys
import os
import builtin_modules
from help_console import help_shell

builtin_modules_names = ['help', 'echo', 'test']

async def shell(history=[]) -> None:
    """
    the DonutScript shell.
    """
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
                # only add a new line
                # if the loop is not at the last one.
                res += v + ('\n' if i != (len(history) - 1) else '')
            print(res)
            await shell()

        # get the function for that
        # command if any, for built in modules
        if text.split(' ')[0] in builtin_modules_names:
            x = getattr(builtin_modules, text.split(' ')[0])
            x(text)

        if text == '.exit':
            sys.exit(0)

def clear_console():
    """
    Clears the console before starting the shell.
    """
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
