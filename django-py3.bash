apt-get update
apt-get dist-upgrade
locale-gen ru_RU.UTF-8
apt-get install apache2 mc nano libapache2-mod-wsgi-py3 python3-pip python3-imaging -y
pip3 install django
pip3 install django-mptt
mkdir /var/www/log
