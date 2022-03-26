import json
from typing import Tuple
import pathlib

def read_config(path: str) -> Tuple[str, bool]:
    prompt = ''
    should_welcome = True

    absolute_path = pathlib.Path(path).absolute()
    if path is not None and path.strip() != "":
        with open(absolute_path) as r:
            res = json.loads(r.read())
        
            if res['prompt'] == None:
                prompt = '{cwd} → '
            else:
                prompt = res['prompt']

            try:
                if res['displayWelcomeMessage'] == False: 
                    should_welcome = False
            except KeyError:
                should_welcome = True
    else:
        prompt = '{cwd} → '

    return prompt, should_welcome
