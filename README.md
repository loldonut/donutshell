# DonutShell

A Custom Shell I made in Python for fun, which means it sucks lmao

## Installation
currently, the Only way to use this program is to clone this repo

and run `python main.py` (or `py main.py`)

Example:

```sh-session
git clone https://github.com/loldonut/donutshell
cd donutshell

python main.py
# or
py main.py
```

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

`"displayWelcomeMessage": true | false` - (bool) If it should display the 'DonutScript' welcome message.

### Values for Config

`{cwd}` - The Current Working Directory
