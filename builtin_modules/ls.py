import os

def ls(text: str) -> None:
    split_text = text.split(' ')
    path = '.'
    if len(split_text) > 0: 
        try:
            path = split_text[1]
        except:
            pass

    try:
        files = os.listdir(path)

        for file in files:
            print(file)
    except (FileNotFoundError, PermissionError) as e:
        error_str = str(e)

        # Permission Denied Error
        if error_str.startswith('[Errno 13]'):
            print(f'Cannot Access \'{path}\' (Permission Denied)')
        elif error_str.startswith('[Errno 2]'):
            print('No such directory as ' + path)
