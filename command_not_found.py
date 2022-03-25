def command_not_found(text: str) -> None:
    command = text.split(' ')[0]

    print(f'No command called \'{command}\'')
