import os

def ls(text: str) -> None:
    split_text = text.split(' ')
    path = '.'
    if len(split_text) > 0: 
        try:
            path = split_text[1]
        except IndexError: pass

    try:
        files = os.listdir(path)

        for file in files:
            print(file)
    except PermissionError:
        print(f'Cannot Access \'{path}\' (Permission Denied)')
    except FileNotFoundError:
        print('No such directory as ' + path)
