#!/usr/bin/python3
#this script contains writes a fabfile to distribute archive to a web server
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """ this function will distribute an archive into a web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
