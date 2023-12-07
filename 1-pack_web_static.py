#!/usr/bin/python3
"""
A Fabric script that generates a tgz archive
Usage: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create a compressed archive of the web_static folder
    Returns:
        str: The path to the generated archive if successful, otherwise None
    """
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = 'web_static_' + current_time + '.tgz'
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))
    if result.failed:
        return None
    else:
        return archive
