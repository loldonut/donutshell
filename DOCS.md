# The Documentation for DonutShell

## Table of Contents

- [Built-in Commands](#built-in-commands)
- [Config](#config)

## Built-in Commands

`help` - Shows the Built-in commands and it's description.

`echo <...text>` - Prints whatever is in `texts`

`history` - Shows the history of the commands you have ran

`ls [path]` - Prints the list of files in `path` if not print the current working directory

## Config

You can change the configuration in `config.json`

Config Example:

```json
{
    "prompt": "{cwd} -> "
}
```

_Make sure to add a space at the end._

The Shell looks for the `prompt` value in the config and sets that as the input message.

If there is no `prompt` value the default is

`{cwd} → `

### Config File

All of the possible Config value

`"prompt": "value"` - (str) The input message

`"displayWelcomeMessage": true | false` - (bool) If it should display the 'DonutScript' welcome message. (`true` by default)

### Values for Config

`{cwd}` - The Current Working Directory
