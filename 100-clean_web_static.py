#!/usr/bin/python3
import os
from fabric.api import *

<<<<<<< HEAD
env.hosts = ['100.25.19.204', '54.157.159.85']


def do_clean(number=0):
    """Deletes out-of-date archives with exceptions"""
=======
env.hosts = ['107.21.41.165', '54.164.97.140']


def do_clean(number=0):
    """Delete out-of-date archives
    """
>>>>>>> 76fec58ef53b10240b16544d83fa0faaa2e595e5
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
