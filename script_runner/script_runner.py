#!//usr/bin/env python

import json
import subprocess
from base64 import b64encode, b64decode

def decode(json_obj):
    j = json.loads(json_obj)
    script = b64decode(j['script'])
    with open("script-1.sh", 'w') as f:
        f.write(script)
    run("script-1.sh")

def run(script):
    proc = subprocess.Popen(["chmod", "+x", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if out:
        print out
    if err:
        print err
    proc = subprocess.Popen(["./{0}".format(script)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if out:
        print out
    if err:
        print err
    print "retruncode: {0}".format(proc.returncode)

if __name__ == "__main__":
    with open("script.sh", 'r') as f:
        script = f.read()
        data = {
                'script': b64encode(script)
                }
        decode(json.dumps(data))
