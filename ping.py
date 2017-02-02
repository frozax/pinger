#!/usr/bin/env python3

import colorama
import subprocess
import sys
from datetime import datetime
from time import sleep

if len(sys.argv) <= 1:
    print("Usage: ./ping.py <host>")
    sys.exit(1)
colorama.init()

host = sys.argv[1]
cmd_line = "ping -n -c1 %s > /dev/null" % host

def compute_up():
    try:
        subprocess.check_call(cmd_line, shell=True)
        return True
    except:
        return False


def log(msg):
    full_msg = "%s: %s is %s" % (str(datetime.now()), host, msg)
    with open("%s.log" % host, "at") as f:
        f.write(full_msg + "\n")
    print((colorama.Fore.RED if msg == "down" else colorama.Fore.GREEN) + full_msg)


last_up = None
while True:
    cur_up = compute_up()
    if cur_up != last_up:
        last_up = cur_up
        log("up" if last_up else "down")
    sleep(10)
