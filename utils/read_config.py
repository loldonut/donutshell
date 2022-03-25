import json
from typing import Tuple

def read_config() -> Tuple[str, bool]:
    prompt = ''
    should_welcome = True

    with open('./config.json') as r:
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

    return prompt, should_welcome
