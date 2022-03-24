async def help_shell():
    res = ''
    builtin_commands = [
        {
            'name': 'history',
            'description': 'Shows the history of the commands you have ran. If any.'
        },
        {
            'name': 'echo',
            'description': 'Prints things.'
        }
    ]

    res += 'Built-in Commands\n'
    for x in builtin_commands:
        res += f'{x["name"]}:\n    {x["description"]}\n'
    return res
