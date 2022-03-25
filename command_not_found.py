from typing import List
from difflib import get_close_matches

def command_not_found(
    text: str, 
    valid_commands: List[str]
) -> None:
    """
    Prints a command not found error, 
    and try to find a similar command 
    based on the command you have entered
    """
    command = text.split(' ')[0]
    possible_matches = get_close_matches(command, valid_commands)
    res = f'No command called \'{command}\''

    if possible_matches != []:
        res += ', did you mean:\n'
        for i, possible_match in enumerate(possible_matches):
            res += f'    {possible_match}' + ('\n' if i != (len(possible_matches) - 1) else '')

    print(f'{res}')
