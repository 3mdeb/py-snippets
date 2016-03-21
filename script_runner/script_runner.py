#!//usr/bin/env python

import json
from base64 import b64encode, b64decode

def decode(b64str):
    pass

def run(script):
    pass

if __name__ == "__main__":
    with open("script.sh", 'r') as f:
        script = f.read()
        decode(b64encode(script))
