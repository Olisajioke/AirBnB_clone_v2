#!/usr/bin/python3
"""
Fabric script for deploying an archive to web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.197.21.228', '3.85.1.40']


def do_pack():
    """
    Creates a compressed archive of the web_static folder
    Returns:
        str: The path to the generated archive or None if unsuccessful
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        my_file = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(my_file))
        return my_file
    except IOError:
        return None


def do_deploy(archive_path):
    """
    Distributes the generated archive to the web servers and deploys it
    Args:
        archive_path (str): The path to the archive to be deployed
    Returns:
        bool: True if successful, False otherwise
    """
    if not exists(archive_path):
        return False
    try:
        f_n = archive_path.split("/")[-1]
        flda_n = f_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, flda_n))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(f_n, path, flda_n))
        run('sudo rm /tmp/{}'.format(f_n))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, flda_n))
        run('sudo rm -rf {}{}/web_static'.format(path, flda_n))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, flda_n))
        return True
    except IOError:
        return False


def deploy():
    """
    Orchestrates the process of generating and deploying the archive
    Returns:
        bool: True if successful, False otherwise
    """
    archive_path = do_pack()
    if not exists(archive_path):
        return False
    return do_deploy(archive_path)
