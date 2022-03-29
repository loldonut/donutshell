import os

def cd(text: str) -> None:
    usage = 'usage: cd <new_dir>'

    new_dir = ''
    try:
        new_dir = text.split(' ')[1]
    except IndexError:
        print(f'No directory provided.\n\n{usage}')
        return

    try:
        os.chdir(new_dir)
    except FileNotFoundError:
        print(f'Directory \'{new_dir}\' does not exist.')
