#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.197.21.228', '3.85.1.40']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        f_n = archive_path.split("/")[-1]
        flda_n = f_n.split(".")[0]
        my_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(my_path, flda_n))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f_n, my_path, flda_n))
        run('rm /tmp/{}'.format(f_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(my_path, flda_n))
        run('rm -rf {}{}/web_static'.format(my_path, flda_n))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(my_path, flda_n))
        return True
    except IOError:
        return False
