#!/usr/bin/python3
"""
Module that deletes out-of-date archives
"""

import os
from fabric.api import *

env.hosts = ['54.197.21.228', '3.85.1.40']


def do_clean(number=0):
    """
    Removes out-of-date archives based on the given number.
    Args:
        number (int): The number of archives to keep.
                      Keeps the most recent 'number' of archives.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    for nums in range(number):
        archives.pop()

    with lcd("versions"):
        for arch in archives:
            local("rm ./{}".format(arch))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [x for x in archives if "web_static_" in x]
        for nums in range(number):
            archives.pop()

        for arch in archives:
            run("rm -rf ./{}".format(arch))
