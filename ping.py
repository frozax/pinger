#!/usr/bin/env python3

import subprocess
import sys

if len(sys.argv) <= 1:
    print("Usage: ./ping.py <host>")
    sys.exit(1)

host = sys.argv[1]
print(host)
