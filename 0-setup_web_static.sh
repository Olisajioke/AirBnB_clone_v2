#!/usr/bin/env bash
# This script automates the setup of web servers for deploying a static website (web_static) by ensuring Nginx is installed

if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

if ! [ -d "/data/web_static/releases/test" ]; then
    sudo mkdir -p /data/web_static/{releases/test,shared}
    sudo touch /data/web_static/releases/test/index.html
    echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

    sudo rm -rf /data/web_static/current
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current

    sudo chown -R ubuntu:ubuntu /data/

    CONFIG_BLOCK="location /hbnb_static {\n\talias /data/web_static/current/;\n}"
    sudo sed -i "/listen 80 default_server/a $CONFIG_BLOCK" /etc/nginx/sites-enabled/default

    sudo service nginx restart

    exit 0
fi
