#!/usr/bin/env python

import asyncio
import sys
import os
import atexit
import argparse

from . import builtin_modules
from .utils import (
    command_not_found,
    read_config,
    help_shell,
)

# Built-in Modules that the Built-in modules can handle
# TODO: Combine these two Variable
builtin_modules_names = ['help', 'echo', 'ls', 'clear']
# For all the built-in modules
# to detect if a valid command has been entered
all_builtin_module_names = [
    'help', 
    'history',
    'clear',
    'echo',
    'ls',
]

parser = argparse.ArgumentParser(
            prog='donutshell',
            description='A Shell built in Python',
            allow_abbrev=False
        )

parser.add_argument('--config', 
                  type=str, 
                  help='(Optional) Custom Configuration JSON file',
                  action='store',
            )

args = parser.parse_args()
file_path = args.config if args.config is not None else ''

prompt_res, should_welcome = read_config(file_path)

async def shell(history=[]) -> None:
    """
    the DonutScript shell.
    """
    cwd_split = os.getcwd().split('/')
    cwd = cwd_split[len(cwd_split) - 1]

    prompt = prompt_res.replace('{cwd}', cwd)

    while True:
        try:
            text = input(prompt) 
        except KeyboardInterrupt:
            sys.exit(0)

        if text.strip() == "":
            await shell()
        else:
            history.append(text)

        cmdName = text.split(' ')[0]

        if cmdName not in all_builtin_module_names:
            command_not_found(text, all_builtin_module_names)
            await shell()

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

def clear_console() -> None:
    """
    Clears the console before starting the shell.
    """
    if os.name in ('nt', 'dos'):
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')

__version__ = '0.0.1rc3'

def main():    
    # Print a tab for it
    # to not exit right at
    # the input message
    proper_exit = lambda: print('\t')
    atexit.register(proper_exit)

    try:
        clear_console()
        if should_welcome == True:
            print(f'DonutShell v{__version__}')

        asyncio.run(shell())
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

if __name__ == '__main__':
    main()
