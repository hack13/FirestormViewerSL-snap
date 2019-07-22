#!/usr/bin/env python3

import os.path
import subprocess
import os
import re

def main():
    subprocess.call(['wget','https://downloads.firestormviewer.org/linux/Phoenix_Firestorm-releasex64_x86_64_6.2.4.57588.tar.xz'])

    subprocess.call(['tar','-xf','Phoenix_Firestorm-releasex64_x86_64_6.2.4.57588.tar.xz'])

    subprocess.call(['rm','-rf','Phoenix_Firestorm-releasex64_x86_64_6.2.4.57588.tar.xz'])
main()